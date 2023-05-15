import time
start_time = time.time()

print ("Hello")
print("World!!!")
print ("Hello World!!!")

# ini comment gak bakal keluar di output
a = 10

print(a)
print(time.time() - start_time, "detik")

import datetime as dt
hari_ini = dt.datetime.today()

print(hari_ini)
print(f"Hari ini adalah hari : {hari_ini:%a}")