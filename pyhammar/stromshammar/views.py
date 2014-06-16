from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.

# indexsidan
def index(request):

    context_dict = {}

    return render_to_response("index.html", context_dict, context_instance = RequestContext(request))

# foreningsinformation
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

# fritidsaktiviteter
def boule(request):

    context_dict = {}

    return render_to_response("boule.html", context_dict, context_instance = RequestContext(request))

def fest(request):

    context_dict = {}

    return render_to_response("fest.html", context_dict, context_instance = RequestContext(request))

def fiske(request):

    context_dict = {}

    return render_to_response("fiske.html", context_dict, context_instance = RequestContext(request))

def golf(request):

    context_dict = {}

    return render_to_response("golf.html", context_dict, context_instance = RequestContext(request))

# ovrigt
def kontakt(request):

    context_dict = {}

    return render_to_response("kontakt.html", context_dict, context_instance = RequestContext(request))

def historia(request):

    context_dict = {}

    return render_to_response("historia.html", context_dict, context_instance = RequestContext(request))

def masonry(request):

    context_dict = {}

    return render_to_response("masonry.html", context_dict, context_instance = RequestContext(request))

def fragorosvar(request):

    context_dict = {}

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
