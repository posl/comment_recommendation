def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(s)
    cnt = 0
    for i in range(10):
        for j in range(n):
            if i == int(s[j][i]):
                cnt += 1
                break
    print(cnt)

if __name__ == '__main__':
    main()