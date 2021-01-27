my_list = [57, -56, 13.2, 'Строка', True, None, {4, 234, 45.8, 'word'}, [5, 7], range(11)]
for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")




my_list = [57, -56, 13.2, 'Строка', True, None, {4, 234, 45.8, 'word'}, [5, 7], range(11)]

def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return


my_type(my_list)
