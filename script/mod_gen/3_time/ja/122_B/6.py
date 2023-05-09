def main():
    s = input()
    ans = 0
    now = 0
    for i in s:
        if i in "ACGT":
            now += 1
        else:
            now = 0
        ans = max(ans, now)
    print(ans)

if __name__ == '__main__':
    main()