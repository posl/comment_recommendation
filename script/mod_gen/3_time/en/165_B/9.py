def main():
    X = int(input())
    ans = 0
    i = 100
    while i < X:
        i = i + i // 100
        ans += 1
    print(ans)
main()
