from os import environ


SESSION_CONFIGS = [
    dict(
        name='dictator',
        display_name="Dictador Basico",
        app_sequence=['dictator', 'payment_info'],
        num_demo_participants=2,
    ),
    dict(
        name='real_effort_numbers',
        display_name="Add up two numbers",
        app_sequence=['real_effort_numbers'],
        num_demo_participants=4,
    ),
    dict(
        name="matrices",
        display_name="Juego del Dictador Parrett",
        num_demo_participants=2,
        app_sequence=['intro', 'survey', "real_effort", 'payment_info'],
        task='matrix',
        attempts_per_puzzle=1,
    ),
    #dict(
    #    name='survey', app_sequence=['survey', 'payment_info'], num_demo_participants=1
    #),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['is_dropout']
SESSION_FIELDS = ['params']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'PEN'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '8280685766045'

INSTALLED_APPS = ['otree']

