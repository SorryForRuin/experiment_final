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
    name_in_url = 'IQ_test_decr'
    players_per_group = 10
    num_rounds = 1
    fix_payment = 4
    fix_payment_survey = 4
    decrease_in_payment = 3
    variable_payment_coef = 2
    payment_per_correct_answer = 1
    correct_answer1 = 8
    correct_answer2 = 4
    correct_answer3 = 5
    correct_answer4 = 6
    correct_answer5 = 2
    correct_answer6 = 7
    correct_answer7 = 1
    correct_answer8 = 5
    correct_answer9 = 2
    correct_answer10 = 5

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    correct_answer = models.IntegerField()
    combined_score = models.IntegerField(initial=0)
    answer_entered1 = models.IntegerField(label="Q1 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered2 = models.IntegerField(label="Q2 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered3 = models.IntegerField(label="Q3 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered4 = models.IntegerField(label="Q4 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered5 = models.IntegerField(label="Q5 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered6 = models.IntegerField(label="Q6 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered7 = models.IntegerField(label="Q7 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered8 = models.IntegerField(label="Q8 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered9 = models.IntegerField(label="Q9 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered10= models.IntegerField(label="Q10 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    score1 = models.IntegerField(initial=0)
    score2 = models.IntegerField(initial=0)
    score3 = models.IntegerField(initial=0)
    score4 = models.IntegerField(initial=0)
    score5 = models.IntegerField(initial=0)
    score6 = models.IntegerField(initial=0)
    score7 = models.IntegerField(initial=0)
    score8 = models.IntegerField(initial=0)
    score9 = models.IntegerField(initial=0)
    score10 = models.IntegerField(initial=0)
    result = models.IntegerField(initial=0)
    noisy_feedback1 = models.IntegerField(initial=0)
    noisy_feedback2 = models.IntegerField(initial=0)
    noisy_feedback3 = models.IntegerField(initial=0)
    current_player = models.IntegerField(initial=0)
    NFresult1 = models.IntegerField(initial=0)
    NFresult2 = models.IntegerField(initial=0)
    NFresult3 = models.IntegerField(initial=0)
    ConfirmQ1 = models.IntegerField(
        label="Please enter how many players you performed BETTER than",
        choices=[3, 2, 1, 0])
    ConfirmQ2 = models.IntegerField(
        label="Please enter how many players you performed WORSE than",
        choices=[3, 2, 1, 0])
    # ConfirmQ3 = models.StringField(
       # label="Please enter whether the THIRD participant you were comared against had performed better, worse or achived the same result",
       # choices=["I have performed BETTER than that player", "I have performed IDENTICALLY compared to that player that player", "I have performed WORSE than that player"])
    confirm_check1 = models.BooleanField()
    confirm_check2 = models.BooleanField()
    # confirm_check3 = models.BooleanField(initial=False)
    likelihood1 = models.FloatField(label="Please state this in percent. Do not write percent sign")
    likelihood2 = models.FloatField(label="Please state this in percent. Do not write percent sign")
    div_l1 = models.FloatField(initial=0)
    div_l2 = models.FloatField(initial=0)
    rank = models.IntegerField(initial=0)
    res = models.IntegerField(initial=0)
    flg_upper_group = models.IntegerField(initial=0)
    payoff1 = models.FloatField(initial=0)
    payoff2 = models.FloatField(initial=0)
    actual_payoff = models.FloatField(initial=0)
    gender = models.StringField(
        label="Please state your gender",
        choices=["Male", "Female", "Other", "Prefer not ot say"])
    age = models.StringField(
        label="Please select your age bracket",
        choices=["18-24", "25-30", "30-49", "larger than 49", "Prefer not ot say"])
    education = models.StringField(
        label="Please state your highest obtained level of education",
        choices=["High school or lower", "Bachelor degree", "Master degree", "PhD degree", "Other",
                 "Prefer not ot say"])
    employment = models.StringField(
        label="Please state your current state of employment",
        choices=["Employed", "Unemployed", "Student", "Prefer not ot say"])
    marriage = models.StringField(
        label="Please state your current marital status",
        choices=["Single", "Married", "Other", "Prefer not ot say"])
