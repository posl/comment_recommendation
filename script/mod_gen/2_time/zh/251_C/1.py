def main():
    n = int(input())
    dic = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s in dic:
            if dic[s][0] < t:
                dic[s] = (t, i)
        else:
            dic[s] = (t, i)
    ans = sorted(dic.items(), key=lambda x: (-x[1][0], x[1][1]))
    print(ans[0][1][1] + 1)

if __name__ == '__main__':
    main()