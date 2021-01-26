from datacenter.models import *


def fix_marks(schoolkid):
    try:
        child = Schoolkid.objects.filter(full_name__contains=schoolkid).get()
    except Schoolkid.DoesNotExist:
        raise ValueError("Такого ученика не существует")
    new_marks = Mark.objects.filter(schoolkid=child,
                                    points__lte=3).update(points=5)
    return new_marks


def remove_chastisements(schoolkid):
    try:
        child = Schoolkid.objects.filter(full_name__contains=schoolkid).get()
    except Schoolkid.DoesNotExist:
        raise ValueError("Такого ученика не существует")
    deleted_chastisement = Chastisement.objects.filter(schoolkid=child).delete()
    return deleted_chastisement


def create_commendation(schoolkid, lesson):
    commendation_text = ["Молодец!", "Великолепно!",
                         "Именно этого я давно ждал от тебя!",
                         "Потрясающе!", "Я вижу, как ты стараешься!",
                         "Очень хороший ответ!",
                         "Прекрасно!", "Отлично!", "Хорошо!", "Я поражен!"]

    try:
        child = Schoolkid.objects.filter(full_name__contains=schoolkid).get()
    except Schoolkid.DoesNotExist:
        raise ValueError("Такого ученика не существует")
    child_lessons = Lesson.objects.filter(year_of_study=child.year_of_study,
                                          group_letter=child.group_letter,
                                          subject__title=lesson)
    child_lesson = child_lessons.order_by("-date").first()
    if child_lesson is None:
        return "Такого урока не существует"
    lesson_date = child_lesson.date
    lesson_teacher = child_lesson.teacher
    commendation = Commendation.objects.filter(created=lesson_date,
                                               schoolkid=child,
                                               subject__title=lesson,
                                               teacher=lesson_teacher).first()
    if commendation is None:
        new_commendation = Commendation.objects.create(text=random.choice(commendation_text),
                                                       created=lesson_date,
                                                       schoolkid=child,
                                                       subject=child_lesson.subject,
                                                       teacher=lesson_teacher)
        return new_commendation
    else:
        return "В этом уроке уже есть похвала, попробуй другой"



