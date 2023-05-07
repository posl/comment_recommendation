def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s.append('end')
    count = 0
    ans = 0
    for i in range(n):
        if s[i] == s[i+1]:
            count += 1
        else:
            ans += int(count*(count+1)/2)
            count = 0
    print(ans)

if __name__ == '__main__':
    main()