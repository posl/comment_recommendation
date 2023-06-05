def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    min = 0
    for i in range(N):
        if min == A[i]:
            min += 1
    print(min)
