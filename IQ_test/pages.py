from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Instructions(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
class IQ_test1(Page):
    form_model = "player"
    form_fields = ["answer_entered1"]


    def before_next_page(self):
        if Constants.correct_answer1 == self.player.answer_entered1:
            self.player.score1 = Constants.payment_per_correct_answer

class IQ_test2(Page):
    form_model = "player"
    form_fields = ["answer_entered2"]

    def before_next_page(self):
        if Constants.correct_answer2 == self.player.answer_entered2:
            self.player.score2 += Constants.payment_per_correct_answer

class IQ_test3(Page):
    form_model = "player"
    form_fields = ["answer_entered3"]

    def before_next_page(self):
        if Constants.correct_answer3 == self.player.answer_entered3:
            self.player.score3 += Constants.payment_per_correct_answer

class IQ_test4(Page):
    form_model = "player"
    form_fields = ["answer_entered4"]

    def before_next_page(self):
        if Constants.correct_answer4 == self.player.answer_entered4:
            self.player.score4 += Constants.payment_per_correct_answer

class IQ_test5(Page):
    form_model = "player"
    form_fields = ["answer_entered5"]

    def before_next_page(self):
        if Constants.correct_answer5 == self.player.answer_entered5:
            self.player.score5 += Constants.payment_per_correct_answer

class IQ_test6(Page):
    form_model = "player"
    form_fields = ["answer_entered6"]

    def before_next_page(self):
        if Constants.correct_answer6 == self.player.answer_entered6:
            self.player.score6 += Constants.payment_per_correct_answer

class IQ_test7(Page):
    form_model = "player"
    form_fields = ["answer_entered7"]

    def before_next_page(self):
        if Constants.correct_answer7 == self.player.answer_entered7:
            self.player.score7 += Constants.payment_per_correct_answer

class IQ_test8(Page):
    form_model = "player"
    form_fields = ["answer_entered8"]

    def before_next_page(self):
        if Constants.correct_answer8 == self.player.answer_entered8:
            self.player.score8 += Constants.payment_per_correct_answer

class IQ_test9(Page):
    form_model = "player"
    form_fields = ["answer_entered9"]

    def before_next_page(self):
        if Constants.correct_answer9 == self.player.answer_entered9:
            self.player.score9 += Constants.payment_per_correct_answer

class IQ_test10(Page):
    form_model = "player"
    form_fields = ["answer_entered10"]

    def before_next_page(self):
        if Constants.correct_answer10 == self.player.answer_entered10:
            self.player.score10 += Constants.payment_per_correct_answer

class ResultsWaitPage(WaitPage):
    form_model = "player"



    # group_by_arrival_time = True
    def vars_for_template(self):
        self.player.combined_score = self.player.score1 + self.player.score2 + self.player.score3 + self.player.score4 + self.player.score5 + self.player.score6 + self.player.score7 + self.player.score8 + self.player.score9 + self.player.score10
        current_player = self.player.id_in_group

    def after_all_players_arrive(self):
        results = []
        for p in self.group.get_players():
            res = p.score1 + p.score2 + p.score3 + p.score4 + p.score5 + p.score6 + p.score7 + p.score8 + p.score9 + p.score10
        players = self.group.get_players()
        # to do descending, use -p.age
        players.sort(key=lambda p: -p.res)
        for i in range(len(players)):
            rank = i + 1
            players[i].rank = rank

        for p in self.group.get_players():
            other_players = set(self.group.get_players())
            other_players.remove(p)
            p2, p3, p4 = random.sample(other_players, 3)
            # resP = p.score1 + p.score2 + p.score3 + p.score4 + p.score5 + p.score6 + p.score7 + p.score8 + p.score9 + p.score10
            # resP2 = p2.score1 + p2.score2 + p2.score3 + p2.score4 + p2.score5 + p2.score6 + p2.score7 + p2.score8 + p2.score9 + p2.score10
            # resP3 = p3.score1 + p3.score2 + p3.score3 + p3.score4 + p3.score5 + p3.score6 + p3.score7 + p3.score8 + p3.score9 + p3.score10
            # resP4 = p4.score1 + p4.score2 + p4.score3 + p4.score4 + p4.score5 + p4.score6 + p4.score7 + p4.score8 + p4.score9 + p4.score10
            resP = p.rank
            resP2 = p2.rank
            resP3 = p3.rank
            resP4 = p4.rank

            if resP > resP2:
                p.NFresult1 = 0
            # elif resP == resP2:
            #     p.NFresult1 = 1
            elif resP < resP2:
                p.NFresult1 = 2

            if resP > resP3:
                p.NFresult2 = 0
            elif resP < resP3:
                p.NFresult2 = 2

            if resP > resP4:
                p.NFresult3 = 0
            elif resP < resP4:
                p.NFresult3 = 2

            if p.rank <= 2:
                p.flg_upper_group = 1
            else:
                p.flg_upper_group = 0



class Feedback(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True



class FeedbackAgain(Page):
    def is_displayed(self):
        if self.player.confirm_check1 is False and self.player.confirm_check2 is False and self.player.confirm_check3 is False:
            return False
        else:
            return True


class Results(Page):
    #class used for testing
    def is_displayed(self):
        if self.round_number == 1:
            return True

        if self.participant.vars["failed_check"] == False:
            return False
        else:
            return True

    def vars_for_template(self):
        self.player.combined_score = self.player.score1 + self.player.score2 + self.player.score3 + self.player.score4 + self.player.score5 + self.player.score6 + self.player.score7 + self.player.score8 + self.player.score9 + self.player.score10
        if self.player.rank <= 5:
            self.player.payoff1 = Constants.fix_payment - Constants.variable_payment_coef * (1 - (self.player.likelihood1 / 100)) * (1 - (self.player.likelihood1 / 100))
            self.player.payoff2 = Constants.fix_payment - Constants.variable_payment_coef * (1 - (self.player.likelihood2 / 100)) * (1 - (self.player.likelihood2 / 100))
        else:
            self.player.payoff1 = Constants.fix_payment - Constants.variable_payment_coef * (0 - (self.player.likelihood1 / 100)) * (0 - (self.player.likelihood1 / 100))
            self.player.payoff2 = Constants.fix_payment - Constants.variable_payment_coef * (0 - (self.player.likelihood2 / 100)) * (0 - (self.player.likelihood2 / 100))

        payoff_set = [self.player.payoff1, self.player.payoff2, Constants.fix_payment_survey]
        self.player.actual_payoff = random.choice(payoff_set)
        self.player.div_l1 = self.player.likelihood1 / 100
        self.player.div_l2 = self.player.likelihood2 / 100
        return {
            "likelihood1": self.player.likelihood1,
            "likelihood2": self.player.likelihood2,
            "div_l1": self.player.div_l1,
            "div_l2": self.player.div_l2,
            "rank": self.player.rank,
            "payoff1": self.player.payoff1,
            "payoff2": self.player.payoff2,
            "actual_payoff": self.player.actual_payoff
        }

class Confirm(Page):
    form_model = "player"
    form_fields = ["ConfirmQ1", "ConfirmQ2"]

    def is_displayed(self):

        if self.round_number == 1:
            return True


    def before_next_page(self):

        if self.player.ConfirmQ1 == 3:
            if self.player.NFresult1 == 2 and self.player.NFresult2 == 2 and self.player.NFresult3 == 2:
                self.player.confirm_check1 = False
                q1 = 1
            else:
                self.player.confirm_check1 = True
                q1 = 0
        if self.player.ConfirmQ1 == 2:
            if self.player.NFresult1 == 2 and self.player.NFresult2 == 2 and self.player.NFresult3 == 0:
                self.player.confirm_check1 = False
                q1 = 1
            elif self.player.NFresult1 == 0 and self.player.NFresult2 == 2 and self.player.NFresult3 == 2:
                self.player.confirm_check1 = False
                q1 = 1
            elif self.player.NFresult1 == 2 and self.player.NFresult2 == 0 and self.player.NFresult3 == 2:
                self.player.confirm_check1 = False
                q1 = 1
            else:
                self.player.confirm_check1 = True
                q1 = 0

        if self.player.ConfirmQ1 == 1:
            if self.player.NFresult1 == 2 and self.player.NFresult2 == 0 and self.player.NFresult3 == 0:
                self.player.confirm_check1 = False
                q1 = 1
            elif self.player.NFresult1 == 0 and self.player.NFresult2 == 2 and self.player.NFresult3 == 0:
                self.player.confirm_check1 = False
                q1 = 1
            elif self.player.NFresult1 == 0 and self.player.NFresult2 == 0 and self.player.NFresult3 == 2:
                self.player.confirm_check1 = False
                q1 = 1
            else:
                self.player.confirm_check1 = True
                q1 = 0

        if self.player.ConfirmQ1 == 0:
            if self.player.NFresult1 == 0 and self.player.NFresult2 == 0 and self.player.NFresult3 == 0:
                self.player.confirm_check1 = False
                q1 = 1
            else:
                self.player.confirm_check1 = True
                q1 = 0

        if self.player.ConfirmQ1 + self.player.ConfirmQ2 != 3:
            self.player.confirm_check2 = True
            q2 = 0
        else:
            self.player.confirm_check2 = False
            q2 = 1



    # def ConfirmQ1_error_message(player, values):
    #
    #     if values["ConfirmQ1"] + values["ConfirmQ2"] != player.number_of_res:
    #         return 'You entered the numbers wrong'



        # if self.player.confirm_check1 is True or self.player.confirm_check2 is True:
        #     self.participant.vars["failed_check"] = True
        # else:
        #     self.participant.vars["failed_check"] = False



# class ConfirmAgain(Page):
#     form_model = "player"
#     form_fields = ["ConfirmQ1", "ConfirmQ2", "ConfirmQ3"]
#
#     def is_displayed(self):
#         if self.player.confirm_check1 is False and self.player.confirm_check2 is False and self.player.confirm_check3 is False:
#             return False
#         else:
#             return True
#
#     def before_next_page(self):
#
#         if self.player.ConfirmQ1 == "I have performed BETTER than that player":
#             if self.player.NFresult1 == 2:
#                 self.player.confirm_check1 = False
#             else:
#                 self.player.confirm_check1 = True
#         if self.player.ConfirmQ1 == "I have performed IDENTICALLY compared to that player that player":
#             if self.player.NFresult1 == 1:
#                 self.player.confirm_check1 = False
#             else:
#                 self.player.confirm_check1 = True
#         if self.player.ConfirmQ1 == "I have performed WORSE than that player":
#             if self.player.NFresult1 == 0:
#                 self.player.confirm_check1 = False
#             else:
#                 self.player.confirm_check1 = True
#
#         if self.player.ConfirmQ2 == "I have performed BETTER than that player":
#             if self.player.NFresult2 == 2:
#                 self.player.confirm_check2 = False
#             else:
#                 self.player.confirm_check2 = True
#         if self.player.ConfirmQ2 == "I have performed IDENTICALLY compared to that player that player":
#             if self.player.NFresult2 == 1:
#                 self.player.confirm_check2 = False
#             else:
#                 self.player.confirm_check2 = True
#         if self.player.ConfirmQ2 == "I have performed WORSE than that player":
#             if self.player.NFresult2 == 0:
#                 self.player.confirm_check2 = False
#             else:
#                 self.player.confirm_check2 = True
#
#         if self.player.ConfirmQ3 == "I have performed BETTER than that player":
#             if self.player.NFresult3 == 2:
#                 self.player.confirm_check3 = False
#             else:
#                 self.player.confirm_check3 = True
#         if self.player.ConfirmQ3 == "I have performed IDENTICALLY compared to that player that player":
#             if self.player.NFresult3 == 1:
#                 self.player.confirm_check3 = False
#             else:
#                 self.player.confirm_check3 = True
#         if self.player.ConfirmQ3 == "I have performed WORSE than that player":
#             if self.player.NFresult3 == 0:
#                 self.player.confirm_check3 = False
#             else:
#                 self.player.confirm_check3 = True
#
#         if self.player.confirm_check1 is True or self.player.confirm_check1 is True or self.player.confirm_check1 is True:
#             self.participant.vars["failed_check"] = True
#         else:
#             self.participant.vars["failed_check"] = False
# class FailCheck(Page):
#     def is_displayed(self):
#         if self.player.confirm_check1 is False and self.player.confirm_check2 is False and self.player.confirm_check3 is False:
#             return False
#         else:
#             return True
class CombinedResults(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


    def vars_for_template(self):
        self.player.combined_score = self.player.score1 + self.player.score2 + self.player.score3 + self.player.score4 + self.player.score5 + self.player.score6 + self.player.score7 + self.player.score8 + self.player.score9 + self.player.score10
        return {
            "combined_payoff":self.player.combined_score
        }
class Likelihood1(Page):
    form_model = "player"
    form_fields = ["likelihood1"]

    # @staticmethod
    # def likelihood1_error_message(player, values):
    #     if values['likelihood1'] > 100 :
    #         return 'The likelihood should lie between 0 and 100'
    #     if values['likelihood1'] < 0 :
    #         return 'The likelihood should lie between 0 and 100'


class Likelihood2(Page):
    form_model = "player"
    form_fields = ["likelihood2"]
    # def likelihood2_error_message(player, values):
    #     if values["likelihood2"] > 100 or values["likelihood2"] < 0:
    #         return 'The likelihood should lie between 0 and 100'

class SurveyQuestions(Page):
    form_model = "player"
    form_fields = ["gender", "age", "education", "employment", "marriage"]


page_sequence = [Instructions, IQ_test1, IQ_test2, IQ_test3, IQ_test4, IQ_test5, IQ_test6,
                 IQ_test7, IQ_test8, IQ_test9, IQ_test10, ResultsWaitPage,
                 Likelihood1, Feedback, Confirm, Likelihood2, Results, SurveyQuestions]
