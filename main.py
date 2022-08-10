from datetime import datetime
from random import randint, choice
from collections import defaultdict


def generate_data() -> datetime.date:
    num_of_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    year = randint(1995, 2010)
    month = randint(1, 12)
    day = randint(1, num_of_days[month])
    return datetime(year, month, day).date()


def get_week_day(birthday_index: int) -> str:
    week_days = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    return week_days[birthday_index]


def get_current_year(birthday: datetime.date) -> datetime.date:
    return datetime(year=datetime.now().year, month=birthday.month, day=birthday.day).date()


def get_birthdays_per_week(users: list):
    greeting_list = defaultdict(list)
    for user_dict in users:
        for name, birthday in user_dict.items():
            current_year_date = get_current_year(birthday)
            birthday_index = current_year_date.weekday()
            weekday = get_week_day(birthday_index)
            if weekday == 'Sunday' or weekday == 'Saturday':
                weekday = 'Monday'
            greeting_list[weekday].append(name)
    for weekday, birthday_boy in greeting_list.items():
        print(f'{weekday}: '+', '.join(birthday_boy))


users = [{'Billy': generate_data()},
         {'David': generate_data()},
         {'Elizabeth': generate_data()}]


if __name__ == '__main__':
    get_birthdays_per_week(users)

