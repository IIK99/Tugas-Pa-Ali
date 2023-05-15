# Qeue adalah antrian data

from collections import deque

Queu = deque ([1,2,3,4,5,6])
print('Data now: ',Queu)

#Add data
Queu.append(7)
print('Data in: ',7)
print('Data now: ',Queu)

Queu.append(8)
print('Data in: ',8)
print('Data now: ',Queu)

# Pop data atau mengurangi data
Out = Queu.popleft()
print('Data out: ',Out)
print('Data now: ',Queu)

Out = Queu.popleft()
print('Data out: ',Out)
print('Data now: ',Queu)

Out = Queu.popleft()
print('Data out: ',Out)
print('Data now: ',Queu)