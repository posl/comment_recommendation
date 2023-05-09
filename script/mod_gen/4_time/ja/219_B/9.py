def main():
    # T = input()
    # S1 = input()
    # S2 = input()
    # S3 = input()
    T = "1321"
    S1 = "mari"
    S2 = "to"
    S3 = "zzo"
    ans = ""
    for i in range(len(T)):
        if T[i] == "1":
            ans += S1
        elif T[i] == "2":
            ans += S2
        elif T[i] == "3":
            ans += S3
    print(ans)

if __name__ == '__main__':
    main()