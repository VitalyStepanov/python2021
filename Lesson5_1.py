my_f = open("text_5.2.txt", "w", encoding="utf-8")
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break
my_f.close()
my_f = open("text_5.2.txt", 'r')
content = my_f.readlines()
print(content)
my_f.close()