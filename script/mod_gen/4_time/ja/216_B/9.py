def main():
    # N = int(input())
    # s = []
    # t = []
    # for i in range(N):
    #     s.append(input().split()[0])
    #     t.append(input().split()[1])
    # # print(s)
    # # print(t)
    # for i in range(N):
    #     for j in range(i+1, N):
    #         if s[i] == s[j] and t[i] == t[j]:
    #             print("Yes")
    #             exit()
    # print("No")
    N = int(input())
    s = set()
    for i in range(N):
        s.add(input())
    if len(s) == N:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()