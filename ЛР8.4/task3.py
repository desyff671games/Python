import datetime as dt

start_moment = dt.datetime(2024, 1, 12, 10, 10, 0)
current_moment = dt.datetime(2024, 5, 22, 23, 20, 0)

total_time = current_moment - start_moment


print(total_time)