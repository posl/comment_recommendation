def main():
    N, Q = map(int, input().split())
    S = input()
    lr_list = []
    for i in range(Q):
        lr_list.append(list(map(int, input().split())))
    for i in range(Q):
        l = lr_list[i][0]
        r = lr_list[i][1]
        count = 0
        for j in range(l-1, r-1):
            if S[j] == 'A' and S[j+1] == 'C':
                count += 1
        print(count)

if __name__ == '__main__':
    main()