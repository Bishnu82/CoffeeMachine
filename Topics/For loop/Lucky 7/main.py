n = int(input())
lst = list()

for _ in range(n):
    lst.append(int(input()))

for x in lst:
    if x % 7 == 0:
        print(x ** 2)
