def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [False for _ in range(2001)]
    for i in range(N):
        B[A[i]] = True
    for i in range(2001):
        if not B[i]:
            print(i)
            break
