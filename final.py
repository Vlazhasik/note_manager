note_1=[]
name=input('Введите имя пользователя: ')
info=input('Укажите содержание заметки: ')
status=input('Укажите статус заметки: ')
created_date=input('Введите дату добавления заметки в формате дд.мм.гг.: ')
issue_date=input('Введите крайний день выполнения заметки в формате дд.мм.гг.: ')
title_1=input('Введите заголовок 1: ')
title_2=input('Введите заголовок 2: ')
note_1.append(name)
note_1.append(info)
note_1.append(status)
note_1.append(created_date)
note_1.append(issue_date)
note_2=[title_1,title_2]
note_1.append(note_2)
print(note_1)




