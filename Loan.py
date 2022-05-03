import math


class Loan:
    def __init__(self, principal=None, interest=None, annuity=None, periods=None):
        self.principal = principal
        self.interest = float(interest/100 / (12 * 1))
        self.annuity = annuity
        self.periods = periods

    def calculate_annuity(self):
        i_pow = math.pow((1 + self.interest), self.periods)
        mult = (self.interest * i_pow) / (i_pow - 1)
        self.annuity = math.ceil(self.principal * mult)
        return self.annuity

    def calculate_months(self):
        return math.ceil(self.principal / self.annuity)

    def calculate_months_w_interest(self):
        form = self.annuity / (self.annuity - self.interest * self.principal)
        self.periods = math.ceil(math.log(form, 1 + self.interest))
        return self.periods

    def calculate_monthly_pay(self):
        self.annuity = math.ceil(self.principal / self.periods)
        last_pay = math.ceil(self.principal - (self.periods - 1) * self.annuity)
        return [self.annuity, last_pay]

    def calculate_principal(self):
        i_pow = math.pow((1 + self.interest), self.periods)
        div = (self.interest * i_pow) / (i_pow - 1)
        self.principal = math.ceil(self.annuity / div)
        return self.principal
