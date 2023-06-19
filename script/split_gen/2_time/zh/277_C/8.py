def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(min(B) - max(A) + 1 if min(B) - max(A) + 1 > 0 else 0)
