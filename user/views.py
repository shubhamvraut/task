from io import BytesIO

import qrcode
from PIL import Image, ImageDraw
from django.core.files import File
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic


# Create your views here.
from forms.user_form import UserForm
from user.models import User


class Index(generic.TemplateView):
    model = User
    form_class = UserForm
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        user_detail = User.objects.get(id=1)

        return render(self.request, self.template_name, {"form": form, 'user_detail': user_detail})

class UpdateUser(generic.CreateView):

    def get(self,request):
        user = User.objects.get(pk=id)
        form = UserForm(instance=user)
        return render(self.request, 'user_update.html',{"form": form})

    def post(self, request,id):
        user=User.objects.get(pk=id)
        form = UserForm(request.POST, files=request.FILES, instance=user)

        if form.is_valid():
            user = form.save(request)
            user.save()
            print(user.profile_pic)
        else:
            print(form.errors)
        return redirect('')

class UpdateUser(generic.UpdateView):

    def get(self,request,id):
        user = User.objects.get(pk=id)
        form = UserForm(instance=user)
        return render(self.request, 'user_update.html',{"form": form})

    def post(self, request,id):
        user=User.objects.get(pk=id)
        form = UserForm(request.POST, files=request.FILES, instance=user)

        if form.is_valid():
            user = form.save(request)
            user.save()
            print(user.profile_pic)
        else:
            print(form.errors)
        return redirect('')


class GenerateQrcode(generic.CreateView):

    def get(self,request,id):

        user = User.objects.get(id=id)
        qrcode_image = qrcode.make(id)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_image)
        fname = 'qrcode-%s.png' % user.id
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        user.qr_code.save(fname, File(buffer), save=True)
        return redirect('')