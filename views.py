

from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from django.http import JsonResponse

from jmfsutils import FileException, walk_format



class JsonResponseNotFound (JsonResponse):
	"""
	Json version of HttpResponseNotFound - HTTP status 404
	The Json payload contains the error message 'msg'.
	"""

	def __init__(self, msg):
		msg_dict = { 'msg' : msg }
		JsonResponse.__init__(self, msg_dict)
		self.status_code = 404



def ls( request ):
	"""
	Returns a JSON representation of the contents of a filesystem path.
	POST to this view with a 'path' parameter 
		- either the name of a path or an absolute or relative 
		filesystem path.
	Any errors are returned as HTTP 404 with a JSON payload containing 
		a 'msg' attribute.
	"""

	path = request.POST['path']

	
	try:
		w = walk_format(path) 
		return JsonResponse( w )

	except FileException as fe:
				
		return JsonResponseNotFound( fe.msg )



@ensure_csrf_cookie
def index(request):
	"""
	Displays the Simple File Browser single page application.
	Includes a CSRF cookie so that CSRF protection can be 
		applied to POST requests issued by the application in 
		an AJAX context.
	"""
	return render( request, 'index.html')

