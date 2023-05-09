def main():
    S = input()
    ans = 0
    for i in range(10000):
        num = str(i).zfill(4)
        flag = 1
        for j in range(10):
            if S[j] == 'o' and not str(j) in num:
                flag = 0
                break
            elif S[j] == 'x' and str(j) in num:
                flag = 0
                break
        ans += flag
    print(ans)

if __name__ == '__main__':
    main()