from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SurveyQuestions(Page):
    form_model = "player"
    form_fields = ["gender", "age", "education", "employment", "marriage"]




page_sequence = [SurveyQuestions]
