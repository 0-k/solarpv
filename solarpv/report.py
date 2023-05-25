from dataclasses import asdict

from solarpv import balance, generation
from solarpv.parameters import Parameters


def create_income_report(params):
    generation_data = generation.request_solar_data(params)
    capacity = params["capacity"]
    income = balance.calc_fit_income(capacity, 0.13, generation_data.sum() / capacity)
    return income


if __name__ == "__main__":
    parameters = Parameters(lat=50.125, lon=8.814, capacity=1.0, tilt=5, azim=180)
    print(create_income_report(asdict(parameters)))
