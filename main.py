from datetime import datetime
expectedformat = '%Y-%m-%d %H:%M:%S'
dt = input('Enter a valid date and time: ')
try:
    dt = datetime.strptime('2019-Jan-03 22:04:00', expectedformat)
except ValueError:
    print('Invalid datetime')
print(dt)