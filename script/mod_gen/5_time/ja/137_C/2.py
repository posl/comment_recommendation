def main():
    N = int(input())
    ans = 0
    dic = {}
    for i in range(N):
        s = input()
        s = ''.join(sorted(s))
        if s in dic:
            ans += dic[s]
            dic[s] += 1
        else:
            dic[s] = 1
    print(ans)

if __name__ == '__main__':
    main()