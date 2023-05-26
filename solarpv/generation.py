import json
from dataclasses import asdict

import pandas as pd
import requests
from parameters import Technical


def request_solar_data(technical: Technical):
    api_base = "https://www.renewables.ninja/api/"
    session = requests.session()
    url = api_base + "data/pv"
    response = session.get(url, params=asdict(technical))
    parsed_response = json.loads(response.text)
    return pd.read_json(json.dumps(parsed_response["data"]), orient="index").squeeze()


if __name__ == "__main__":
    parameters = Technical(lat=50.125, lon=8.814, capacity=1.0, tilt=5, azim=180)
    data = request_solar_data(parameters)
