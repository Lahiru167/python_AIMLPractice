import datetime

b_day = datetime.date(1990, 5, 17)

print(b_day)

today  = datetime.date.today()

print(today)

print(b_day.strftime('%A,%B %d, %Y'))

age = today - b_day
print(age)

print(today.weekday())
print(today.isoweekday())