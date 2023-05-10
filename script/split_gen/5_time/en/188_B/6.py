def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    res = 0
    for i in range(N):
        res += A[i]*B[i]
    if res == 0:
        print("Yes")
    else:
        print("No")
