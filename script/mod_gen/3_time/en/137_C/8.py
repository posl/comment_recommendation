def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s.sort()
    count = 0
    tmp = 0
    for i in range(N):
        if i == 0:
            tmp = 1
        elif s[i] == s[i-1]:
            tmp += 1
        else:
            count += tmp * (tmp - 1) // 2
            tmp = 1
    count += tmp * (tmp - 1) // 2
    print(count)

if __name__ == '__main__':
    main()