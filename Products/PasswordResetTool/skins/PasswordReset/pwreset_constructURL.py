## Script (Python) "pwreset_constructURL.py"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##title=Create the URL where passwords are reset
##parameters=randomstring
from zExceptions import Forbidden
if container.REQUEST['PUBLISHED'] is script:
   raise Forbidden('Script may not be published.')

host = container.absolute_url()
return "%s/passwordreset/%s" % (host, randomstring)
