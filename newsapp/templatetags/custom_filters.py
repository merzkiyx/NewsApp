from django import template
import re

register = template.Library()


unwanted_words = ["дурак", "гад", "подлец"]

@register.filter
def censor(value):

    censored_value = value


    for word in unwanted_words:

        pattern = re.compile(rf'\b{word}\b', re.IGNORECASE)

        censored_value = pattern.sub('*', censored_value)

    return censored_value