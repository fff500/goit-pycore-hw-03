import datetime

def get_days_from_today(date):
    try:
        today = datetime.date.today()
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

        return int((today - date).days)
    except ValueError:
        print(f"Date {date} is not a valid date")