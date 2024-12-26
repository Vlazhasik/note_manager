list_1 = []
while True:
        heading = str(input('Введите заголовок (или оставьзе пустым для завершения: '))
        list_1.append(heading)
        print('Заголовок добавлен!')
        if heading == '':
                print('Ввод закончен')
                break
print(list_1)



