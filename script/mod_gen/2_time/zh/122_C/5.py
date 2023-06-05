def main():
    S = input()
    ans = 0
    cnt = 0
    for s in S:
        if s in ['A', 'C', 'G', 'T']:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()