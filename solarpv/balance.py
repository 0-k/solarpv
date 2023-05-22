def calc_annuity_factor(rate, years):
    if years <= 0:
        raise ValueError("Years cannot be smaller or equal to 0.")
    if rate == 0:
        return 1 / years
    return ((1 + rate) ** years * rate) / ((1 + rate) ** years - 1)


def calc_fit_income(size, fit, full_load_hours):
    return size * fit * full_load_hours


def calc_annuity(rate, years, invest):
    return invest * calc_annuity_factor(rate, years)


def calc_yearly_surplus(income, annuity, other_expenses):
    return income - annuity - other_expenses
