def main():
    n = int(input())
    lr = []
    for _ in range(n):
        lr.append(list(map(int,input().split())))
    lr.sort()
    ans = []
    ans.append(lr[0])
    for i in range(1,n):
        if ans[-1][1] >= lr[i][0]:
            ans[-1][1] = max(ans[-1][1],lr[i][1])
        else:
            ans.append(lr[i])
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])

if __name__ == '__main__':
    main()