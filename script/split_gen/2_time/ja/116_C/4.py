def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    while True:
        i = 0
        while i < N:
            if H[i] == 0:
                i += 1
                continue
            l = i
            while i < N and H[i] > 0:
                i += 1
            r = i
            ans += 1
            for j in range(l, r):
                H[j] -= 1
        if i == N:
            break
    print(ans)
