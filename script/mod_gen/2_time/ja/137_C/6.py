def main():
    N = int(input())
    s = [input() for _ in range(N)]
    s.sort()
    cnt = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if len(s[i]) != len(s[j]):
                break
            if sorted(s[i]) == sorted(s[j]):
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()