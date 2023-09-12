import json
from itertools import chain

import pandas

from marketing_data_cleaning import DATA_FOLDER_PATH


def chain_for_dataframe(filename, write_file=True):
    """
    Regroups subsets of dictionnaries together

    >>> [[{...}], [{...}]]
    ... [{...}, {...}]
    """
    with open(DATA_FOLDER_PATH / filename, mode='r', encoding='utf-8') as f:
        chained_values = list(chain(*json.load(f)))
        df = pandas.DataFrame(chained_values)

        if write_file:
            df.to_json(
                DATA_FOLDER_PATH / 'chained_output.json',
                force_ascii=False,
                orient='records'
            )
        return df
