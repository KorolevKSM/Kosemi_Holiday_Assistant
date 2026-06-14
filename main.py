from config import load_dotenv
load_dotenv()

from database import create_tables, get_today_birthdays
from templates import get_random_template
from notifier import send_email

def main():
    create_tables()
    birthdays = get_today_birthdays()
    if not birthdays:
        print('Сегодня нет именинников.')
        return
    for name, category, email in birthdays:
        if not email:
            print(f"Пропускаю {name} — нет email.")
            continue
        template = get_random_template(category)
        message = template.format(name=name)
        subject = f"С днём рождения, {name}!"
        print(f"Отправляю {name}: {message}")
        send_email(email, subject, message)

if __name__ == '__main__':
    main()