def f(n):
    if n % 2 == 0:
        return n/2
    elif n % 3 == 0:
        return n/3
    else:
        return -1
N = int(input())
A = list(map(int,input().split()))
count = 0
while True:
    for i in range(N):
        if f(A[i]) != -1:
            A[i] = f(A[i])
        else:
            break
    else:
        count += 1
    if i != N-1:
        break
print(count)

if __name__ == '__main__':
    f()