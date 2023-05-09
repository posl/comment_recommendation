def main():
    S = input()
    ans = 0
    for i in range(10**4):
        i = str(i).zfill(4)
        for j in range(len(S)):
            if S[j] == "o" and str(j) not in i:
                break
            elif S[j] == "x" and str(j) in i:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()