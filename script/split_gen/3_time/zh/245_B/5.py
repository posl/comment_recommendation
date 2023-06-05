def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    i = 0
    while i < N:
        if A[i] != i:
            print(i)
            break
        i += 1
    if i == N:
        print(N)
