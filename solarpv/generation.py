import json

import pandas as pd
import requests


def request_solar_data(params):
    api_base = "https://www.renewables.ninja/api/"
    session = requests.session()
    url = api_base + "data/pv"
    response = session.get(url, params=params)
    parsed_response = json.loads(response.text)
    return pd.read_json(json.dumps(parsed_response["data"]), orient="index").squeeze()


if __name__ == "__main__":
    parameters = {
        "lat": 34.125,
        "lon": 39.814,
        "date_from": "2019-01-01",
        "date_to": "2019-12-31",
        "dataset": "merra2",
        "capacity": 1.0,
        "system_loss": 0.1,
        "tracking": 0,
        "tilt": 35,
        "azim": 180,
        "format": "json",
    }
    data = request_solar_data(parameters)
    print(data)
