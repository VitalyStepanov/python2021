def task_3():
    wages = {}
    try:
        with open("text_3.txt", "r", encoding="utf-8") as my_file:
            for line in my_file:
                wages[line.split()[0]] = float(line.split()[1])
            print('Зработная плата меньше 20000: ')
        for name, wage in wages.items():
            if wage < 20000:
                print(name)
        print(f'Средняя заработная плата: {sum(wages.values()) / len(wages)}')
    except IOError:
        print('что то пошло не так')
    except:
        print('все пропало!!!!')


task_3()
print('список меньше всех получивших')
