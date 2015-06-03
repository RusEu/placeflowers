from django.shortcuts import render,render_to_response
from models import Flower
from django.http import HttpResponse,HttpResponseRedirect
from PIL import Image, ImageDraw , ImageFont
import io,os
from urllib2 import urlopen
from random import randint
from django.conf import settings
# Create your views here.
def index(request):
	return render_to_response("index.html")

def with_width(request,width):
	random_image = Flower.objects.order_by('?').first()
	costum_image = Image.open(random_image.image.url)
	costum_image = costum_image.convert("RGBA")
	size = costum_image.size
	width= int(width)
	landscape = False
	if size[0]<size[1]:
		landscape = True
	if landscape:
		costum_image = costum_image.resize( [width,width] )
	else:
		costum_image = costum_image.resize( [width,width] )
	response = HttpResponse(content_type="image/png")
	costum_image.save(response, "PNG")
	random_number = str(randint(1,99))
	costum_image.save(os.path.join("static/tmp/image"+random_number+".png"),"PNG")
	return response

def width_and_height(request,width,height):
	random_image = Flower.objects.order_by('?').first()
	costum_image = Image.open(random_image.image.url)
	costum_image = costum_image.convert("RGBA")
	width = int(width)
	height = int(height)
	size = costum_image.size
	landscape = False
	if size[0]<size[1]:
		landscape = True
	if landscape:
		costum_image = costum_image.resize( [width,height] )
	else:
		costum_image = costum_image.resize( [width,height] )
	response = HttpResponse(content_type="image/png")
	costum_image.save(response, "PNG")
	random_number = str(randint(1,99))
	costum_image.save(os.path.join("static/tmp/image"+random_number+".png"),"PNG")
	return response