def main():
    S = input()
    ans = 0
    count = 0
    for i in range(len(S)):
        if S[i] in "ACGT":
            count += 1
            ans = max(ans, count)
        else:
            count = 0
    print(ans)

if __name__ == '__main__':
    main()