import itertools


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return year, 29
    else:
        return year, 28


years = []
for i in range(1816, 2018):
    years.append(is_leap_year(i))

day_numbers = []
for i in years:
    month_lengths = [31, i[1], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for j in range(len(month_lengths)):
        for l in range(month_lengths[j]):
            day_numbers.append((i[0], j+1, l))

print(day_numbers[int(input())])
print(day_numbers[1000])
print(day_numbers[2000])
print(day_numbers[3000])
print(day_numbers[4000])
print(day_numbers[5000])
