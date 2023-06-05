def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(abs(x))
    A.append(abs(y))
    A.sort()
    for i in range(N+1):
        if A[i] == A[i+1]:
            print('No')
            return
    print('Yes')
