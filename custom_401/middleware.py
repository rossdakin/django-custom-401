from django.core.exceptions import PermissionDenied
from django.shortcuts import render_to_response
from django.template import RequestContext
from custom_401 import TEMPLATE_PATH

class Custom401Middleware(object):
    def process_exception(self, request, exception):
        if isinstance(exception, PermissionDenied):
            return render_to_response(TEMPLATE_PATH, { 'exception': exception },
                                      context_instance = RequestContext(request))
        return None
