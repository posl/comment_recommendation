def main():
    n = int(input())
    s = [input() for i in range(n)]
    ans = 0
    for i in range(10):
        for j in range(n):
            if s[j][i] != str((i+1)%10):
                break
        else:
            continue
        ans = i
        break
    print(ans)

if __name__ == '__main__':
    main()