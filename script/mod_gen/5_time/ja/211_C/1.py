def main():
    S = input()
    #print(S)
    ans = 0
    cnt = 0
    for s in S:
        if s == 'c' and cnt == 0:
            cnt += 1
        elif s == 'h' and cnt == 1:
            cnt += 1
        elif s == 'o' and cnt == 2:
            cnt += 1
        elif s == 'k' and cnt == 3:
            cnt += 1
        elif s == 'u' and cnt == 4:
            cnt += 1
        elif s == 'd' and cnt == 5:
            cnt += 1
        elif s == 'a' and cnt == 6:
            cnt += 1
        elif s == 'i' and cnt == 7:
            cnt += 1
            ans += 1
        else:
            continue
    print(ans % (10**9 + 7))

if __name__ == '__main__':
    main()