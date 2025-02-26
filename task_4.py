import datetime

def get_upcoming_birthdays(users):
    cur_year = datetime.datetime.now().year
    today = datetime.date.today().timetuple().tm_yday
    greetings = []

    for user in users:
        b_day_date = datetime.datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        b_day_number = b_day_date.timetuple().tm_yday
        b_day_month = b_day_date.month
        b_day_day = b_day_date.day
        b_day_week_day = datetime.datetime.strptime( \
                str(cur_year) + "." + str(b_day_month) + "." + str(b_day_day), "%Y.%m.%d" \
            ).weekday()

        if today <= b_day_number <= today + 7:
            if b_day_week_day == 5:
                b_day_number += 2
            if b_day_week_day == 6:
                b_day_number += 1
        
        congrats_date = datetime.datetime.strptime(str(cur_year) + "." + str(b_day_number), "%Y.%j").strftime("%Y.%m.%d")
        greetings.append({"name": user['name'], "congratulation_date": congrats_date})

    print(greetings)
    return greetings