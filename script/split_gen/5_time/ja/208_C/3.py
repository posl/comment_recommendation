def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    a = sorted(A)
    b = K // N
    c = K % N
    for i in range(N):
        if i < c:
            print(b+1)
        else:
            print(b)
