from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.StringField(
        label="Please state your gender",
        choices=["Male", "Female", "Other", "Prefer not ot say"])
    age = models.StringField(
        label="Please select your age bracket",
        choices=["18-24", "25-30", "30-49", "larger than 49", "Prefer not ot say"])
    education = models.StringField(
        label="Please state your highest obtained level of education",
        choices=["High school or lower", "Bachelor degree", "Master degree", "PhD degree", "Other", "Prefer not ot say"])
    employment = models.StringField(
        label="Please state your current state of employment",
        choices=["Employed", "Unemployed", "Student", "Prefer not ot say"])
    marriage = models.StringField(
        label="Please state your current marital status",
        choices=["Single", "Married", "Other", "Prefer not ot say"])