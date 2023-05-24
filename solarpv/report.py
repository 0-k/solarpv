from solarpv import generation
from solarpv import balance


def create_income_report(params):
    generation_data = generation.request_solar_data(params)
    capacity = params["capacity"]
    income  = balance.calc_fit_income(capacity, 0.13, generation_data.sum()/capacity)
    return income

if __name__ == '__main__':
    parameters = {
        "lat": 52.44,
        "lon": 13.4,
        "date_from": "2019-01-01",
        "date_to": "2019-12-31",
        "dataset": "merra2",
        "capacity": 10.0,
        "system_loss": 0.1,
        "tracking": 0,
        "tilt": 5,
        "azim": 185,
        "format": "json",
    }
    print(create_income_report(parameters))
