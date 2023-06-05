def S(n):
    a = str(n)
    sum = 0
    for i in a:
        sum += int(i)
    return sum
K = int(input())
n = 1
for i in range(K):
    while S(n) * K != S(n * K):
        n += 1
    print(n)
    n += 1

if __name__ == '__main__':
    S()