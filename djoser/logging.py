from rest_framework_tracking.mixins import BaseLoggingMixin

import inspect

def mixin(obj):
    # Add BaseLogingMixin from drf-tracking in first sequence of mixin to the class
    bases = obj.__bases__
    obj.__bases__ = (BaseLoggingMixin , )
    obj.__bases__ += bases

def add_logging_mixin(module) :
    # Add mixin to the class inside module only 
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):            
            if obj.__module__ == module.__name__:            
                mixin(obj)