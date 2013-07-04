from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):

	return render_to_response('index.html',context_instance=RequestContext(request))

def about(request):
	
	return render_to_response('about.html',context_instance=RequestContext(request))

def instructions(request):
	
	return render_to_response('instructions.html',context_instance=RequestContext(request))

def team(request):
	
	return render_to_response('team.html',context_instance=RequestContext(request))

def privacy(request):
	
	return render_to_response('privacy.html',context_instance=RequestContext(request))

def new_to_muni(request):
	
	return render_to_response('new_to_muni.html',context_instance=RequestContext(request))

def signup(request):
	
	return render_to_response('signup.html',context_instance=RequestContext(request))

def survey(request):
	
	return render_to_response('survey.html',context_instance=RequestContext(request))