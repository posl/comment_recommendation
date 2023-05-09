def main():
    q = int(input())
    a = []
    for i in range(q):
        a.append(list(map(int, input().split())))
    ans = []
    for i in range(q):
        if a[i][0] == 1:
            ans.append([a[i][1]] * a[i][2])
        else:
            print(sum(ans.pop(0)))

if __name__ == '__main__':
    main()