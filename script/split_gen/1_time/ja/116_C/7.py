def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while 1:
        if max(h) == 0:
            break
        i = 0
        while 1:
            if i == N:
                break
            if h[i] != 0:
                break
            i += 1
        l = i
        while 1:
            if i == N:
                break
            if h[i] == 0:
                break
            i += 1
        r = i
        for j in range(l, r):
            h[j] -= 1
        ans += 1
    print(ans)
