def send_email(message, recipient, sender="university.help@gmail.com"):
    if not (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')) or not "@" in recipient:
        print(f'Невозможно отправить письмо с адреса  {sender}  на адрес {recipient}')
        return
    if not (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')) or not "@" in recipient:
        print(f'Невозможно отправить письмо с адреса {sender}  на адрес  {recipient}')
        return
    if not "@" in recipient or not "@" in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    else:
        if sender != "university.help@gmail.com":
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
            return
        else:
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            return



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')