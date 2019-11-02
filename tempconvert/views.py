from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
	return render(request, 'tempconvert/index.html')

@csrf_exempt
def converttemp(request):
	if 'Convert_to_Celsius' in request.POST:

		fahr=request.POST.get('temperature',False)
		celsiusvalue = (int(fahr) - 32) * 5/9
		return celsiusvalue

	elif 'Convert_to_Fahrenheit' in request.POST:

		cels = request.POST.get('temperature',False)
		fahrenheitvalue = (int(cels) * 1.8) + 32
		return fahrenheitvalue

@csrf_exempt
def convert(request):
	context = {'calculated_value': 0}
	context['calculated_value'] = converttemp(request)
	return render(request, 'tempconvert/answer.html',context)