def main():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    ans = []
    for i in range(h):
        if a[i].count('.') != w:
            ans.append(a[i])
    ans = list(map(list, zip(*ans)))
    for i in range(len(ans)):
        print(''.join(ans[i]))

if __name__ == '__main__':
    main()