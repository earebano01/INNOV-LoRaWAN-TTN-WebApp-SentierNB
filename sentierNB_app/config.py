path_db = '/var/ttn_tracker/ttn_tracker_database.db' # Chemin de la base de données SQLite

refresh_period_seconds = 15 # Période de rafraîchissement en secondes

start_lat = 47.6211 # Latitude de départ
start_lon = -65.67496 # Longitude de départ

cluster = "nam1" # Cluster utilisé

application = "sensecap-lora-tracker" # Application utilisée
app_key = "NNSXS.TGFGSOEXIKJROJXVOWTDUUOVWQH76LKAKOPLICI.7VSE4Z6NTIHL5WQBASAB7MX7COYW6CNL66NCVRTH5674DR4ZIKWQ" # Clé d'application

devices = [ # Liste des appareils
    "eui-a8610a34363a9216"
]

gateway_locations = [ # Emplacements des passerelles
    ('Début du sentier', 47.6236834, -65.69033),
    ('Fin du sentier', 47.6133651, -65.67693)
]

bing_api_key = 'AvYvx0oLrNB_CUoKLJibjitGAD7bB4o8i1bJMsPJodKBW2FftQUNSjB-Kfp9aQ8y' # Clé API Bing Maps

def config_app(app):
    # Configuration de l'application Flask pour utiliser la base de données SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{db}'.format(db=path_db)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
