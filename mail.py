from dotenv import load_dotenv
import os
import smtplib

load_dotenv()
sender = os.getenv("EMAIL_LOGIN")
password = os.getenv("EMAIL_PASSWORD")

receiver = input('Введите адрес получателя:')
subject = input('Тема письма:')
friend_name = input('Введите имя друга:')

my_name = 'Aleksandr'
website = 'https://dvmn.org/profession-ref-program/vaultboy21/gOkX0/'

letter = """From: {sender}
To: {receiver}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8"

From: {sender}
To: {receiver}
Subject: {subject}

Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""
letter = letter.format(
    sender=sender,
    receiver=receiver,
    subject=subject,
    friend_name=friend_name,
    my_name=my_name,
    website=website
)

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
server.login(sender, password)
server.sendmail(sender, receiver, letter)
server.quit()

print("Письмо отправлено.")
