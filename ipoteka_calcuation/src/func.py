#Функция расчета итоговой суммы выпдаты по кридету на установленный срок
def sum_to_pay(sum_of_credit, time_to_pay, bid = 0.2):
	res = sum_of_credit
	for i in range(1, time_to_pay+1):
		res *= (1+bid)
	return res	

#Функция расчета ежемесячного платежа по аннуитетной системе кредитования
def payment(sum_of_credit, time_to_pay, bid):
	payment = (sum_of_credit * (bid/12) * (1+(bid/12))**(time_to_pay*12)) / ((1+(bid/12))**(time_to_pay*12) - 1)
	return payment
