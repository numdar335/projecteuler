# task description: https://projecteuler.net/problem=30
import math
sum = 0
for i in range(10,9*9*9*9*9*math.floor(1+math.log10(5)+5*math.log10(9))+1):
  temp, a = 0, len(str(i))
  for j in range(a):
    b = i//10**j%10
    temp += b*b*b*b*b
  if i == temp: sum += temp
print(sum)
