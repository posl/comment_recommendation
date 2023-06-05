def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        else:
            diff = ord(T[i]) - ord(S[i])
            if diff < 0:
                diff = diff + 26
            if diff == 1:
                continue
            else:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()