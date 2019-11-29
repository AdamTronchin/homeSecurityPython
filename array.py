import time
from database import DatabaseBackend

numbers = ["a"]

b = DatabaseBackend()

while 1==2:
 for x in numbers:
  print("Yes")
time.sleep(5)
print(b.readValue())