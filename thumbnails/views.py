from django.shortcuts import render,render_to_response
from models import Flower
from django.http import HttpResponse,HttpResponseRedirect
from PIL import Image, ImageDraw , ImageFont
import io,os
from urllib2 import urlopen
from random import randint
from django.conf import settings
from django.template import RequestContext
from django.core.context_processors import request

# Create your views here.
def index(request):
	return render_to_response("index.html",RequestContext(request))

def recalculate(request):	
	all_images = Flower.objects.all()
	for item in all_images:
		this_image = Image.open(item.image.url)
		size = this_image.size
		this_object = Flower.objects.get(id=item.id)
		if size[0]<size[1]:
			this_object.image_type = "portrait"
		elif size[0]>size[1]:
			this_object.image_type = "landscape"
		else:
			this_object.image_type = "square"
		this_object.save()
	return HttpResponse("All Images Recalculated")
def with_width(request,width):
	random_image = Flower.objects.order_by('?').first()
	costum_image = Image.open(random_image.image.url)
	costum_image = costum_image.convert("RGBA")
	size = costum_image.size
	width= int(width)
	costum_image = costum_image.resize( [width,width] )
	response = HttpResponse(content_type="image/png")
	costum_image.save(response, "PNG")
	return response

def width_and_height(request,width,height):
	if width > height:
		type_image = "landscape"
	elif width < height:
		type_image = "portrait"
	else:
		type_image = "square"
	random_image = Flower.objects.filter(image_type=type_image).order_by('?').first()
	costum_image = Image.open(random_image.image.url)
	costum_image = costum_image.convert("RGBA")
	width = int(width)
	height = int(height)
	size = costum_image.size
	costum_image = costum_image.resize( [width,height] )
	response = HttpResponse(content_type="image/png")
	costum_image.save(response, "PNG")
	return response