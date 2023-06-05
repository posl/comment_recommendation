def S(n):
    sum = 0
    while n>0:
        sum += n%10
        n = n//10
    return sum
k = int(input())
count = 0
n = 1
while True:
    if S(n) == 1:
        n += 9
        continue
    if n%S(n) == 0:
        count += 1
        print(n)
    if count == k:
        break
    n += 1

if __name__ == '__main__':
    S()