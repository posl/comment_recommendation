def main():
    A, B, N = map(int, input().split())
    # print(A, B, N)
    if B <= N:
        x = B - 1
    else:
        x = N
    print(A * x // B - A * (x // B))
