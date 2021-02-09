result = {}
with open('text_6.txt', 'r') as init_f:
    for line in init_f:
        lesson_time = []
        lesson = ([el for el in line.split(" ")])
        for el in lesson:
            lesson_time.append(''.join(i for i in list(el) if i.isdigit()))
        result[line.split(":")[0]] = sum([int(i) for i in lesson_time if i.isdigit()])
print(result)
