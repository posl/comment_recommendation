def main():
    S = input()
    K = int(input())
    s = list(S)
    for i in range(len(s)):
        if s[i] == '1':
            K -= 1
        else:
            break
        if K == 0:
            print(s[i])
            return
    print(s[i])

if __name__ == '__main__':
    main()