def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while True:
        if max(h) == 0:
            break
        else:
            i = 0
            while i < n:
                if h[i] > 0:
                    ans += 1
                    while i < n and h[i] > 0:
                        h[i] -= 1
                        i += 1
                i += 1
    print(ans)
