import math


class Loan:
    def __init__(self, principal):
        self.principal = principal

    def calculate_months(self, monthly):
        return math.ceil(self.principal / monthly)

    def calculate_monthly_pay(self, months):
        m_pay = math.ceil(self.principal / months)
        last_pay = math.ceil(self.principal - (months - 1) * m_pay)
        return [m_pay, last_pay]
