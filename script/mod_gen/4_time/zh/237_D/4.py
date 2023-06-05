def main():
    n = int(input())
    s = input()
    l = 0
    r = 0
    ans = [0]
    for i in range(n):
        if s[i] == 'L':
            l += 1
            ans.insert(l, i+1)
        else:
            r += 1
            ans.insert(l, i+1)
    for i in ans:
        print(i, end=' ')
    print()

if __name__ == '__main__':
    main()