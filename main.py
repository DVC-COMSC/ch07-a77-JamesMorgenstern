
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
num3 = []

if (len(num1) <= len(num2)):
    for i in range(len(num1)):
        num3.append(num1[i])
        num3.append(num2[i])
        j = i

    while (j < len(num2) - 1):
        j += 1
        num3.append(num2[j])
else:
    for i in range(len(num2)):
        num3.append(num1[i])
        num3.append(num2[i])
        j = i

    while (j < len(num1) - 1):
        j += 1
        num3.append(num1[j])

print (num3) 
