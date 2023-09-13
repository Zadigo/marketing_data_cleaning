import pathlib

import dotenv


PROJECT_PATH = pathlib.Path(__file__).parent.absolute()

ENV_PATH = PROJECT_PATH / '.env'

DATA_FOLDER_PATH = PROJECT_PATH / 'data'

BASE_COLUMNS = {
    'linkedin',
    'first_name',
    'last_name',
    'full_name',
    'position',
    'company',
    'company_linkedin',
    'enriched',
    'website'
}

BASE_COLUMNS_WITH_EMAIL = BASE_COLUMNS.update(['courtesy_columns', 'email'])

BASE_AIRTABLE_COLUMNS = {
    'LinkedIn',
    'Civilité', 
    'Prénom', 
    'Nom', 
    'Nom complet', 
    'Poste',
    'Entreprise',
    'Company LinkedIn',
    'Statut enrichissement',
    'Email',
    'Site entreprise',
    'Created'
}


dotenv.load_dotenv(ENV_PATH)
