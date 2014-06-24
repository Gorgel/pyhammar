from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
from .forms import CaptchaWallForm
from models import WallPost, NewsPost, GolfPost, GolfImage, FAQPost, GalleryImage, FiskeImage, FiskePost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

########################################################
#
#
#                      Startsidan
#
#
#########################################################


def index(request):

    news_posts = NewsPost.objects.all().order_by('-date')

    paginator = Paginator(news_posts, 6)

    npost = request.GET.get('page')
    try:
        news_posts = paginator.page(npost)
    except PageNotAnInteger:
        news_posts = paginator.page(1)
    except EmptyPage:
        news_posts = paginator.page(paginator.num_pages)

    context_dict = {'news_posts' : news_posts}

    return render_to_response("index.html", context_dict, context_instance = RequestContext(request))



########################################################
#
#
#                       Information
#
#
#########################################################


def stadgar(request):

    context_dict = {}

    return render_to_response("stadgar.html", context_dict, context_instance = RequestContext(request))

def styrelsen(request):

    context_dict = {}

    return render_to_response("styrelsen.html", context_dict, context_instance = RequestContext(request))

def vattengruppen(request):

    context_dict = {}

    return render_to_response("vattengruppen.html", context_dict, context_instance = RequestContext(request))

def vagogront(request):

    context_dict = {}

    return render_to_response("vagogront.html", context_dict, context_instance = RequestContext(request))

def lagindelning(request):

    context_dict = {}

    return render_to_response("lagindelning.html", context_dict, context_instance = RequestContext(request))


########################################################
#
#
#                       fritidsaktiviteter
#
#
#########################################################


def boule(request):

    context_dict = {}

    return render_to_response("boule.html", context_dict, context_instance = RequestContext(request))

def fest(request):

    context_dict = {}

    return render_to_response("fest.html", context_dict, context_instance = RequestContext(request))

def fiske(request):

    fiske_posts_list = FiskePost.objects.all().order_by('-pub_date')
    fiske_posts = FiskePost.objects.all().order_by('-pub_date')
    fiske_images = FiskeImage.objects.all()
    paginator = Paginator(fiske_posts, 1)


    fpost = request.GET.get('page')
    try:
        fiske_posts = paginator.page(fpost)
    except PageNotAnInteger:
        fiske_posts = paginator.page(1)
    except EmptyPage:
        fiske_posts = paginator.page(paginator.num_pages)

    context_dict = { 'fiske_images' : fiske_images, 'fiske_posts' : fiske_posts, 'fiske_posts_list' : fiske_posts_list}

    return render_to_response("fiske.html", context_dict, context_instance = RequestContext(request))

def golf(request):

    golf_posts_list = GolfPost.objects.all().order_by('-pub_date')
    golf_posts = GolfPost.objects.all().order_by('-pub_date')
    golf_images = GolfImage.objects.all()
    paginator = Paginator(golf_posts, 1)


    gpost = request.GET.get('page')
    try:
        golf_posts = paginator.page(gpost)
    except PageNotAnInteger:
        golf_posts = paginator.page(1)
    except EmptyPage:
        golf_posts = paginator.page(paginator.num_pages)

    context_dict = { 'golf_images' : golf_images, 'golf_posts' : golf_posts, 'golf_posts_list' : golf_posts_list}

    return render_to_response("golf.html", context_dict, context_instance = RequestContext(request))

########################################################
#
#
#                       Ovrigt
#
#
#########################################################


def kontakt(request):

    context_dict = {}

    return render_to_response("kontakt.html", context_dict, context_instance = RequestContext(request))

def historia(request):

    context_dict = {}

    return render_to_response("historia.html", context_dict, context_instance = RequestContext(request))

def masonry(request):

    images = GalleryImage.objects.all()

    context_dict = {'images' : images }

    return render_to_response("masonry.html", context_dict, context_instance = RequestContext(request))


def fragorosvar(request):

    faqs = FAQPost.objects.all()

    context_dict = {'faqs' : faqs }

    return render_to_response("fragorosvar.html", context_dict, context_instance = RequestContext(request))


def forbattring(request):

    context_dict = {}

    return render_to_response("forbattring.html", context_dict, context_instance = RequestContext(request))

def license_bootstrap(request):

    context_dict = {}

    return render_to_response("license_bootstrap.html", context_dict, context_instance = RequestContext(request))

def license_lightbox(request):

    context_dict = {}

    return render_to_response("license_lightbox.html", context_dict, context_instance = RequestContext(request))

########################################################
#
#
#                       Wall
#
#
#########################################################

def wall(request):
    context = RequestContext(request)

    form = CaptchaWallForm(request.POST or None)
    wall_posts = WallPost.objects.all().order_by('-timestamp')
    paginator = Paginator(wall_posts, 10)

    wpost = request.GET.get('page')
    try:
        wall_posts = paginator.page(wpost)
    except PageNotAnInteger:
        wall_posts = paginator.page(1)
    except EmptyPage:
        wall_posts = paginator.page(paginator.num_pages)

    context_dict = {'wall_posts': wall_posts, 'form': form}

    if form.is_valid():
        human = True
        save_it = form.save(commit=False)
        save_it.save()
        return HttpResponseRedirect('thankyou')
    else:
        form = CaptchaWallForm()


    return render_to_response("wall.html",
                              context_dict,
                              context)

def thankyou(request):


    return render_to_response("thankyou.html",
                              locals(),
                              context_instance = RequestContext(request))
