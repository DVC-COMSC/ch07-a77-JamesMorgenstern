
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
num3 = []

for i in range(len(num1)):
    num3.append(num1[i])
    num3.append(num2[i])
    j = i

while (j < len(num2) - 1):
    j += 1
    num3.append(num2[j])

print (num3) 
