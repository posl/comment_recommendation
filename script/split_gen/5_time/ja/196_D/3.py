def main():
    h, w, a, b = map(int, input().split())
    ans = 0
    for i in range(h-a):
        for j in range(b, w):
            ans += 1
    print(ans)
