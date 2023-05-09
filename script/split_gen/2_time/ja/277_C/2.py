def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort(reverse=True)
    B.sort(reverse=True)
    a = A[0]
    b = B[0]
    if a != b:
        print(a+b)
    else:
        a2 = A[1]
        b2 = B[1]
        print(max(a+a2, b+b2))
