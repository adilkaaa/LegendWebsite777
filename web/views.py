from django.shortcuts import render
from .forms import SendToEmailForm, MessageForm
# Create your views here.
from .models import *
from django.core.mail import send_mail
# rest_framework
from rest_framework import viewsets
from .serializers import *

# authorization
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login


def index(request):
    if request.method == 'POST':
        # form = MessageForm(request.POST)
        # form2 = SendToEmailForm(request.POST)
        # if form.is_valid():
        #     form.save()
        # if form2.is_valid():
        #     form2.save()
        if 'mail' in request.POST:
            form = SendToEmailForm(request.POST)
            mail = request.POST['mail']

            send_mail(
                'Adding you to Legend Website',
                'Hi, we are adding you to Legend Website.My congratulations!!!',
                'legendwebsite777gmail.com',
                [mail],
            )
            if form.is_valid():
                form.save()
        else:
            form2 = MessageForm(request.POST)
            if form2.is_valid():
                form2.save()
    form2 = MessageForm()
    form = SendToEmailForm()
    portfolio = Portfolio.objects.all()
    blogs = Blog.objects.all()
    employers = Employer.objects.all()
    return render(request, 'index.html', {'portfolio': portfolio,
                                          'blogs': blogs,
                                          'employers': employers,
                                          'form': form,
                                          'form2': form2
                                          })


def message(request):
    messages = Message.objects.all()[::-1]
    context = {
        'messages': messages
    }
    return render(request, 'message.html', context=context)


# rest_framework

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class SendToEmailViewSet(viewsets.ModelViewSet):
    queryset = SendToEmail.objects.all()
    serializer_class = SendToEmailSerializer


# authorization
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context= self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.BasePermission,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)