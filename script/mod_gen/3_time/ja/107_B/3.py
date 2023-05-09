def main():
    hw = input().split()
    h = int(hw[0])
    w = int(hw[1])
    a = []
    for i in range(h):
        a.append(input())
    ans = []
    for i in range(h):
        if a[i].count('.') != w:
            ans.append(a[i])
    ans2 = []
    for j in range(w):
        tmp = 0
        for i in range(len(ans)):
            if ans[i][j] == '.':
                tmp += 1
        if tmp != len(ans):
            ans2.append(j)
    for i in range(len(ans)):
        for j in ans2:
            print(ans[i][j], end='')
        print()

if __name__ == '__main__':
    main()