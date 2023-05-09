def main():
    S = input()
    ans = "Yes"
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i].isupper():
                ans = "No"
                break
        else:
            if S[i].islower():
                ans = "No"
                break
    print(ans)
main()

if __name__ == '__main__':
    main()