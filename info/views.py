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

def new_to_muni(request):
	
	return render_to_response('new_to_muni.html',context_instance=RequestContext(request))

def signup(request):
	
	return render_to_response('signup.html',context_instance=RequestContext(request))

def survey(request):
	
	return render_to_response('survey.html',context_instance=RequestContext(request))

def contact(request):
	
	return render_to_response('contact.html',context_instance=RequestContext(request))

def install(request):
	
	return render_to_response('install_instructions.html',context_instance=RequestContext(request))

def participation(request):
	
	return render_to_response('participation_instructions.html',context_instance=RequestContext(request))

def widget(request):
	
	return render_to_response('widget_instructions.html',context_instance=RequestContext(request))