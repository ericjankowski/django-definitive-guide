from django.http import HttpResponse
import datetime

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body><p>It is now %s.</p></body></html>" % now
	return HttpResponse(html)

def hours_ahead(request, offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body><p>In %s hour(s), it will be %s.</p></body></html>" % (offset, dt)
	return HttpResponse(html)