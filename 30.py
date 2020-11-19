#task description: https://projecteuler.net/problem=30
import math
sum = 0
for i in range(10,9*9*9*9*9*math.floor(1+math.log10(5)+5*math.log10(9))+1):
  temp = 0
  a = str(i)
  for j in range (1,len(a)+1):
    b = i//10**(j-1)%10
    temp += b*b*b*b*b
  if i == temp: sum += temp
print(sum)
