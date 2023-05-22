from solarpv import balance

cost_per_kw = 700  # EUR/kw
size = 50  # kw
fit = 0.11  # EUR/kw
full_load_hours = 950  # kwh/kw
leasing_contribution_factor = 0.1
invest = cost_per_kw * size


fit_income = balance.calc_fit_income(size, fit, full_load_hours)
annuity = balance.calc_annuity(0.05, 20, invest)
lease = annuity * leasing_contribution_factor
yearly_surplus = balance.calc_yearly_surplus(fit_income, annuity, lease)
