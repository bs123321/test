from datetime import datetime

date_birth = "2007-02-26"

date_birth_data = datetime.date(datetime.strptime(date_birth,"%Y-%m-%d"))
year = date_birth_data.year
now_year = datetime.now().year
age = now_year - year

print(datetime.date(datetime.strptime(date_birth,"%Y-%m-%d")))
print(year)
print(now_year)
print(age)


a = 5
b = 10

print(a // b)