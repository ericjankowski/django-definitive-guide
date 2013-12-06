from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
	# Old Way
	#now = datetime.datetime.now()
	#return render_to_response('current_datetime.html', {'current_date' : now})

	# Using locals()
	current_date = datetime.datetime.now()
	return render_to_response('current_datetime.html', locals())