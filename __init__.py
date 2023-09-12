import pathlib

import dotenv


PROJECT_PATH = pathlib.Path(__file__).parent.absolute()

ENV_PATH = PROJECT_PATH / '.env'

DATA_FOLDER_PATH = PROJECT_PATH / 'data'

BASE_COLUMNS = {
    'company',
    'enriched',
    'full_name',
    'first_name',
    'last_name',
    'company_linkedin',
    'linkedin',
    'position',
    'website'
}

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
