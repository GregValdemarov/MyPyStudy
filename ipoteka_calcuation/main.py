from src import classes


new_credit = classes.Credit(map(int(), (input("Сумма кредита: "), input("Срок кредитования (лет): "), input("Число платежей: "), input("Процентная ставка (по умолчанию 20%): "))))

new_credit.sum_of_credit -= 100000

print(new_credit.sum_of_credit)