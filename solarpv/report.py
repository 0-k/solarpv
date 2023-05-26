from solarpv import balance, generation
from solarpv.parameters import Financial, Technical


def create_income_report(technical: Technical, financial: Financial):
    generation_data = generation.request_solar_data(technical)
    income = balance.calc_fit_income(
        technical.capacity, financial.fit, generation_data.sum() / technical.capacity
    )
    return income


if __name__ == "__main__":
    technical = Technical(lat=50.125, lon=8.814, capacity=1.0, tilt=5, azim=180)
    financial = Financial(fit=0.1)
    print(create_income_report(technical, financial))
