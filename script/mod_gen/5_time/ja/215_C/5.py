def main():
    s, k = input().split()
    k = int(k)
    s = list(s)
    s.sort()
    ans = []
    for i in range(len(s)):
        ans.append(s[i])
        ans += sorted(s[i+1:])
        if len(ans) >= k:
            break
    print("".join(ans[:k]))

if __name__ == '__main__':
    main()