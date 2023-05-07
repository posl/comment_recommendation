def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N-1):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    if N-1 == max(A.count(i) for i in range(1, N+1)):
        print("Yes")
    else:
        print("No")
