from django.conf import settings

from random import choice
from string import ascii_letters, digits

#VARS
SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

AVAIABLE_CHARDS = ascii_letters + digits

#CREATE RANDOM CHARACTERS FOR LINKS
def create_random_code (chars=AVAIABLE_CHARDS):
    
    return "".join(
        [choice(chars) for _ in range(SIZE)]
        )

#CODE TO URL FUNTION:    
def create_shortened_url(model_instance):
    random_code = create_random_code()
    
    model_class = model_instance.__class__
    
    if model_class.objects.filter(short_url=random_code).exists():
        
        return create_shortened_url(model_instance)
    
    return random_code