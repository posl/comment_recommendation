def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        s.append(list(map(int, input().split())))
        p.append(int(input()))
    count = 0
    for i in range(0, 2**N):
        flag = True
        for j in range(M):
            sum = 0
            for m in range(k[j][0]):
                sum += (i >> (s[j][m]-1)) & 1
            if sum % 2 != p[j]:
                flag = False
                break
        if flag:
            count += 1
    print(count)

if __name__ == '__main__':
    main()