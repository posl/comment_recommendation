def main():
    S = input()
    ans = 0
    for i in range(10000):
        num = str(i).zfill(4)
        flag = True
        for j, s in enumerate(S):
            if s == "o" and num[j] not in S:
                flag = False
            if s == "x" and num[j] in S:
                flag = False
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()