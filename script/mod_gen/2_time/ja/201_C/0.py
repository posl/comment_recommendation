def main():
    S = input()
    ans = 0
    for i in range(10000):
        num = str(i).zfill(4)
        flag = True
        for j in range(10):
            if S[j] == "o" and str(j) not in num:
                flag = False
                break
            elif S[j] == "x" and str(j) in num:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()