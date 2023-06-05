def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    child = []
    adult = []
    for i in range(n):
        if s[i] == '0':
            child.append(w[i])
        else:
            adult.append(w[i])
    child.sort()
    adult.sort()
    ch = len(child)
    ad = len(adult)
    if ad == 0:
        print(ch)
        exit()
    if ch == 0:
        print(0)
        exit()
    ans = 0
    for i in range(1, ch+1):
        if i > ad:
            break
        ans = max(ans, sum(child[:ch-i])+sum(adult[:i]))
    print(ans)

if __name__ == '__main__':
    main()