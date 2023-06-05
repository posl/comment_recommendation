def main():
    n = int(input())
    s = []
    for i in range(n):
        l, r = map(int, input().split())
        s.append([l, r])
    s.sort()
    ans = []
    left = s[0][0]
    right = s[0][1]
    for i in range(1, n):
        if right < s[i][0]:
            ans.append([left, right])
            left = s[i][0]
            right = s[i][1]
        else:
            right = max(right, s[i][1])
    ans.append([left, right])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

if __name__ == '__main__':
    main()