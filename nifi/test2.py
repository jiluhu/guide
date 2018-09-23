import json
# import sys
# import traceback
import datetime

input_text = '{"start_time": "2018-04-09 00:00:00", "end_time": "2018-04-09 01:00:00", "meas_type": 2001,"id": "110151000000000974"}'
input_obj = json.loads(input_text)

output_arr = []
start_time = input_obj['start_time']
end_time = input_obj['end_time']
id = input_obj['id']
meas_type = input_obj['meas_type']

date = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
endtime = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

while date < endtime:
    output_obj = {
        "id": id,
        "meas_type": meas_type,
        "val": 0,
        "create_time": date.strftime("%Y-%m-%d %H:%M:%S"),
        "create_day": datetime.datetime.strptime(date.strftime("%Y-%m-%d"), '%Y-%m-%d').strftime(
            "%Y-%m-%d %H:%M:%S"),
        "create_minute": date.strftime("%H:%M:%S")
    }
    if date.strftime("%M") == "00":
        output_obj['vtype'] = '时间'
    elif date.strftime("%M") == "01":
        output_obj['vtype'] = '最大值'
    elif date.strftime("%M") == "02":
        output_obj['vtype'] = '最小值'
    else:
        output_obj['vtype'] = '平均值'
    date = date + datetime.timedelta(minutes=1)
    print(output_obj)
    # Write output content
    #output_arr.append(output_obj)
print (output_arr)

detester = '2018-04-12 00:00:00.0'
count = 0
for i in range(0, 24):
    for j in range(0, 60):
        date = datetime.datetime.strptime(detester, '%Y-%m-%d %H:%M:%S.%f') + datetime.timedelta(
            hours=i) + + datetime.timedelta(minutes=j)
        create_time = date.strftime("%Y-%m-%d %H:%M:%S.%f")
        create_day = datetime.datetime.strptime(date.strftime("%Y-%m-%d"), '%Y-%m-%d').strftime("%Y-%m-%d %H:%M:%S.%f")
        create_minute = date.strftime("%H:%M:%S.%f")
        count = count + 1

date = (datetime.datetime.strptime(detester, '%Y-%m-%d %H:%M:%S.%f') + datetime.timedelta(minutes=1))
# .strftime("%Y-%m-%d %H:%M:%S.%f")
output_obj = {
    "create_time": detester,
    "create_time2": date.strftime("%Y-%m-%d %H:%M:%S.%f"),
    "create_day": datetime.datetime.strptime(date.strftime("%Y-%m-%d"), '%Y-%m-%d').strftime("%Y-%m-%d %H:%M:%S.%f"),
    "create_minute": date.strftime("%H:%M:%S.%f"),
    "create_year": date.year,
    "create_month": date.month,
    # "create_day": date.day,
    "create_hour": date.hour
    # ,
    # "create_minute": date.minute
}
print(date)
