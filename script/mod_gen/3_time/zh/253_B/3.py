def main():
    h,w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    print(s)
    # for i in range(h):
    #     for j in range(w):
    #         if s[i][j] == 'o':
    #             print(i,j)
    #             continue
    #         else:
    #             continue
    # print(s[0][2])
    # print(s[1][0])

if __name__ == '__main__':
    main()