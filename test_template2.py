import sys
from django.template.loader import get_template
from django.template.exceptions import TemplateSyntaxError
import django

try:
    django.setup()
    get_template('recipes/index.html')
    print('Template successfully compiled!')
except Exception as e:
    print('ERROR:', str(e))
    sys.exit(1)
