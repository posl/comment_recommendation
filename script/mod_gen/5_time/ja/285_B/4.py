def main():
    n = int(input())
    s = input()
    ans = []
    for i in range(1,n):
        l = 0
        while i + l < n:
            if s[l] != s[i+l]:
                l += 1
            else:
                break
        ans.append(l)
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()