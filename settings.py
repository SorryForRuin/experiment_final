from os import environ

SESSION_CONFIGS = [
    dict(
       name='survey',
       display_name="Socio-demografic survey",
       num_demo_participants=3,
       app_sequence=['survey']
    ),
    dict(
        name='IQ_test',
        display_name="IQ test containing 10 Raven Matrices (Baseline experiment)",
        num_demo_participants=10,
        app_sequence=['IQ_test']
    ),
    dict(
           name='IQ_test_shock_pos_reinforcement',
           display_name="IQ test containing 10 Raven Matrices (Shock #1 - giving passage about why IQ test good)",
           num_demo_participants=10,
           app_sequence=['IQ_test_shock_pos_reinforcement']
        ),
    dict(
           name='IQ_test_shock_neg_reinforcement',
           display_name="IQ test containing 10 Raven Matrices (Shock #2 - giving passage about why IQ test bad)",
           num_demo_participants=10,
           app_sequence=['IQ_test_shock_neg_reinforcement']
        ),
    dict(
           name='IQ_test_shock_decrease_payoff',
           display_name="IQ test containing 10 Raven Matrices (Shock #3 - basic endowment shock)",
           num_demo_participants=10,
           app_sequence=['IQ_test_shock_decrease_payoff']
        ),
    dict(
        name='IQ_test_shock_reward_for_correct_answer',
        display_name="IQ test containing 10 Raven Matrices (Shock #4 - extra endowment for correct answers)",
        num_demo_participants=10,
        app_sequence=['IQ_test_shock_reward_for_correct_answer']
    ),
    dict(
           name='IQ_test_shock_decrease_payoff_and_reward_for_correct_answer',
           display_name="IQ test containing 10 Raven Matrices (Shock #5 - basic endowment shock + extra endowment for correct answers)",
           num_demo_participants=10,
           app_sequence=['IQ_test_shock_decrease_payoff_and_reward_for_correct_answer']
        ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'q195*+cghn^9fnh(doym_ey1yn-&^4q7pnb@59vn_d083t4j6b'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
