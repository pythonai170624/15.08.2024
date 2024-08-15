from datetime import datetime, timedelta

print('Israel', datetime.now())
print('UTC   ', datetime.utcnow())
print(datetime.now().strftime("%H:%M:%S.%f %Y-%m-%d"))
print(datetime.now().strftime("%H:%M:%S.%f %Y-%B-%d %A"))
print((datetime.now() + timedelta(days=1)).strftime("%H:%M:%S.%f %Y-%B-%d %A"))
print((datetime.now() + timedelta(days=30)).strftime("%H:%M:%S.%f %Y-%B-%d %A"))