def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    a = T[0]
    b = 0
    for i in range(1, N):
        if a > b:
            b += T[i]
        else:
            a += T[i]
    print(max(a, b))
