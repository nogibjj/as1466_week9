"""
Extract a dataset from a URL like Kaggle or data.gov.
JSON or CSV formats tend to work well

Jeopardy dataset
"""
import requests


def extract(
    url="https://raw.githubusercontent.com/nogibjj/as1466_sqlite_lab/main/life%20expectancy%202.csv",
    file_path="data/life_expectancy.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
