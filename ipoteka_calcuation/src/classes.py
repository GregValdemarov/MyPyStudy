from datetime import date, timedelta 
from src import func

class Credit():
	def __init__(self, sum_of_credit, time_to_pay, amm_of_pays, bid = 0.2):
		self.sum_of_credit = sum_of_credit
		self.time_to_pay = timedelta(years = time_to_pay)
		self.start_date = date.today()
		self.cur_paid_sum = 0
		self.rest_sum = func.sum_to_pay(self.sum_of_credit, self.time_to_pay, self.bid)
		self.monthly_paiment = func.payment(self.sum_of_credit, self.time_to_pay, self.bid)
		self.rest_months = timedelta()

	def proceed_payment(self, sum_of_payment = "default"):
		if sum_of_payment == "default":
			sum_of_payment = self.monthly_paiment
		self.rest_sum -= sum_of_payment
		###
