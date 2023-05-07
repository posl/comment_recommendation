def main():
    N = int(input())
    a = [0] * (N-1)
    b = [0] * (N-1)
    for i in range(N-1):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    if a[0] == 1 and b[-1] == N:
        print('Yes')
    else:
        print('No')
