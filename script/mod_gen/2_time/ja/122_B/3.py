def main():
    S = input()
    ans = 0
    count = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            count += 1
        else:
            if count > ans:
                ans = count
            count = 0
    if count > ans:
        ans = count
    print(ans)

if __name__ == '__main__':
    main()