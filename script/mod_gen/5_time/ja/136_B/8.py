def oddDigits(n):
    count = 0
    for i in range(1,n+1):
        if len(str(i))%2 == 1:
            count += 1
    return count
n = int(input())
print(oddDigits(n))
