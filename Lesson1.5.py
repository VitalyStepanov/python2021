revenue = float(input('Введите размер выручки'))
costs = float(input('Введите размер издержек'))

if revenue > costs:
    profit = float(revenue - costs)
    print('Ваша прибыль составила', "{:.2f}".format(profit))
    profitability = float(profit / revenue)
    print('Рентабельность сотавила:', "{:.2f}".format(profitability))
    poulation = int(input('Введите количесвто песонала:'))
    profit_employee = float(profit / poulation)
    print('Прибыль на одного работника составляет:', "{:.2f}".format(profit_employee))
elif revenue < costs:
    loss = float(revenue - costs)
    print('Ваша компания сработала с убытком', "{:.2f}".format(loss))
else:
    print('Ваша компания вышла на точку безубыточности!')
print('Спасибо, что используете нашу прорграмму!')
