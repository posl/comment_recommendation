def main():
    N = int(input())
    a = [0] * N
    b = [0] * N
    for i in range(N-1):
        a[i], b[i] = map(int, input().split())
    a = set(a)
    b = set(b)
    if len(a) == 1 or len(b) == 1:
        print("Yes")
    else:
        print("No")
