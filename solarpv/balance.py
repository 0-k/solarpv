def calc_annuity_factor(rate, years):
    if years <= 0:
        raise ValueError("Years cannot be smaller or equal to 0.")
    if rate == 0:
        return 1/years
    return ((1 + rate) ** years * rate) / ((1 + rate) ** years - 1)




