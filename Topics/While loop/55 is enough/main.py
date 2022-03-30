# put your code here
num = 0
counter = 0
total = 0
average = 0
over = 55
while num != over:
    num = int(input())
    if num != over:
        counter = counter + 1
        total += num
        average = total / counter

print(counter)
print(total)
print(round(average))
