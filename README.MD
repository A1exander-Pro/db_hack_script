# Скрипты для работы с базой данных электронного дневника

## Установка:
- У вас имеется доступ к базе данных электронного дневника.
- Поместите файл __scripts.py__ в корневую папку проекта или скопируйте код в __models.py__
- Далее необходимо в терминале/консоле запустить [Django shell](https://tutorial.djangogirls.org/ru/django_orm/) <br>
```your_directory your_username$ python manage.py shell``` <br>
- Пропишите в ```shell``` импорт моделей и функций, если функции вы скопировали в __models.py__:<br>
```from datacenter.models import *```
- Импотрируйте функции скрипта, если вы положили их отдельным файлом __scripts.py__ в корневую папку, прописав в ```shell```:<br>
```from scripts import *```
- Импортуйте через ```shell```  модуль random:<br>
```import random```

## Как использовать 
- Для испрвления оценок, которые меньше 4х баллов используйте функцию <br> ```fix_marks(schoolkid)```<br>, где __schoolkid__ фамилия и имя ученика. Пример функции: ```fix_marks("Фролов Иван")```. Важно писать имя и фамилию без ошибок, проверьте написание перед запуском скрипта!
- Для удаления всех замечаний используйте функцию <br> ```remove_chastisements(schoolkid)``` <br>, где __schoolkid__ фамилия и имя ученика.
Пример функции: ```remove_chastisements("Фролов Иван")```. Важно писать имя и фамилию без ошибок, проверьте написание перед запуском скрипта!
- Для добавления похвалы к последнему выбранному уроку используйте функцию <br> ```create_commendation(schoolkid, lesson)``` <br>, где __schoolkid__ фамилия и имя ученика, а __lesson__ урок, к которому надо добавить похвалу. Пример функции: <br>```create_commendation("Фролов Иван", "История")``` Важно писать имя, фамилию и названия уровка без ошибок, проверьте написание перед запуском скрипта!

## Возможные ошибки
- Сообщение об ошибке, при которой вы ввели неправильное имя:<br> ```datacenter.models.Schoolkid.DoesNotExist: Schoolkid matching query does not exist.```
- Сообщение об ошибке, если вы не указали фамилию <br>```datacenter.models.Schoolkid.MultipleObjectsReturned: get() returned more than one Schoolkid -- it returned 22!```
- Сообщение об ошибке, если вы неправильно указали урок <br>```AttributeError: 'NoneType' object has no attribute 'date'```

## Project Goals
Код написан в образовательных целях на онлайн курсе для веб разработчиков [dvmn.org](https://dvmn.org/).
