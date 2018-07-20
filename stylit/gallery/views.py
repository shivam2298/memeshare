from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
import base64
from django.core.files.base import ContentFile
from .models import Meme,Comment
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404,HttpResponse,redirect
import json
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required()
def createview(request):
    if request.method == 'POST':
        image_data = request.POST['image']
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        name = request.POST['filename'].split('.')[0]
        data = ContentFile(base64.b64decode(imgstr))
        file_name = name + '.' + ext
        print(type(data))

        meme = Meme()
        meme.author = request.user
        meme.caption = request.POST['caption']
        meme.image.save(file_name, data, save=False)
        meme.save()
        return HttpResponseRedirect('/gallery/index')

    else:
        return render(request, 'gallery/create.html')

def indexview(request):
    memes = Meme.objects.all()
    return render(request, 'gallery/index.html',{'memes':memes})


@login_required()
def likeview(request,id):
    meme = get_object_or_404(Meme,pk=id)
    if request.user.is_authenticated:
        isliked = True
        if request.user in meme.like.all():
            meme.like.remove(request.user)
            isliked = False
        else:
            meme.like.add(request.user)
            isliked = True
        return HttpResponse(json.dumps({'liked': isliked, 'likes': meme.like.all().count()}), content_type="application/json")

@login_required()
def commentview(request,id):
    meme = get_object_or_404(Meme,pk=id)
    if request.user.is_authenticated:
        comment = Comment(author=request.user,comment=request.POST.get('comment'))
        comment.save()
        meme.comments.add(comment)
        return HttpResponse(json.dumps({'added':1,'username':request.user.username,'comment':comment.comment}),
                            content_type="application/json")
    else:
        return HttpResponse(json.dumps({'added': 0}),
                            content_type="application/json")

@login_required()
def createcommentview(request,id):
    meme = get_object_or_404(Meme,pk=id)

    return render(request,'gallery/comment.html',{'meme':meme})


