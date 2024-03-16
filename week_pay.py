name = input()
work_time = int(input())
week_pay = 12000
time_limit = 40
overtime = work_time - time_limit
standard_pay = time_limit * week_pay
overtime_pay = overtime * 18000

print('이름 :', name)
print('일주일간 일한 시간 :', work_time, '시간')
print('오버타임 :', overtime, '시간')
print('주급 :',standard_pay + overtime_pay, '원')
