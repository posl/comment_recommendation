def main():
    S = input()
    ans = 0
    for i in range(10000):
        num = str(i).zfill(4)
        for j in range(10):
            if S[j] == "o" and str(j) not in num:
                break
            elif S[j] == "x" and str(j) in num:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()