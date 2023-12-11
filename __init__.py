import datetime
import os
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


def get_windows_download_folder():
    return pathlib.Path(os.getenv('DOWNLOAD_FOLDER'))


def file_from_download_folder(filename):
    return get_windows_download_folder() / filename


def create_filename(prefix=None):
    if prefix is None:
        prefix = 'v'
    d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    filename = f"{prefix}_{d.replace(' ', '_').replace(':', '-')}"
    return filename


def get_file_absolute_path(prefix=None, extension='csv'):
    filename = create_filename(prefix=prefix)
    path = DATA_FOLDER_PATH / f"{filename}.{extension}"
    return path
