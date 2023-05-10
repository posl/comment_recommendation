def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    max_a = max(A)
    max_b = max(B)
    if max_a < max_b:
        print(max_a)
    else:
        print(max_b)
