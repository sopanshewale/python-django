from datetime import datetime, timedelta
d1 = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
d2 = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')
d3 = datetime.strftime(datetime.now() - timedelta(3), '%Y-%m-%d')

print (d1)
print (d2)
print (d3)
