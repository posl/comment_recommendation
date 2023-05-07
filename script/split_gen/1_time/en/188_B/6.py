def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = 0
    for i in range(N):
        C = C + A[i]*B[i]
    if C == 0:
        print("Yes")
    else:
        print("No")
