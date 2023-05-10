def main():
    # input
    n,k = map(int,input().split())
    s = input()
    # solve
    s = list(s)
    s = list(map(int,s))
    s = [0] + s + [0]
    count = 0
    for i in range(n):
        if s[i] == 1 and s[i+1] == 0:
            count += 1
    count = min(count,k)
    ans = 0
    for i in range(n):
        if s[i] == 0:
            count += 1
        if s[i] == 1:
            count -= 1
        if s[i+count] == 0:
            count -= 1
        if s[i+count] == 1:
            count += 1
        ans = max(ans,count)
    # output
    print(ans)

if __name__ == '__main__':
    main()