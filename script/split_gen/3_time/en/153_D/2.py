def main():
    H = int(input())
    ans = 0
    while H > 0:
        ans += H
        H = H // 2
    print(ans)
