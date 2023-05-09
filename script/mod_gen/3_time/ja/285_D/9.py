def main():
    n = int(input())
    s_t = []
    for i in range(n):
        s_t.append(input().split())
    s_t2 = s_t.copy()
    for i in range(n):
        s_t2[i][0], s_t2[i][1] = s_t2[i][1], s_t2[i][0]
    s_t2.sort()
    for i in range(n):
        s_t[i][0], s_t[i][1] = s_t[i][1], s_t[i][0]
    s_t.sort()
    #print(s_t)
    #print(s_t2)
    for i in range(n):
        if s_t[i][0] != s_t2[i][0] or s_t[i][1] != s_t2[i][1]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()