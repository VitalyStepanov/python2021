second_first = int(input('Введите время в секундах: '))
hours = (second_first // 3600)
minute = (second_first - hours * 3600) // 60
second = second_first % 60

print(f"{hours:02}h, {minute:02}m, {second:02}s")
