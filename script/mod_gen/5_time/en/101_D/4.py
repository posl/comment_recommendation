def S(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum
K = int(input())
count = 0
n = 0
while count < K:
    n += 1
    if n/S(n) >= n/S(n+1):
        count += 1
        print(n)

if __name__ == '__main__':
    S()