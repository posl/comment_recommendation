def main():
    A, B, N = map(int, input().split())
    if N < B:
        x = N
    else:
        x = B-1
    print((A*x)//B - A*(x//B))
