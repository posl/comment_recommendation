def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, 26):
        if ord(S[0]) + i > ord('z'):
            k = ord(S[0]) + i - ord('a')
        else:
            k = i
        if ord(T[0]) == ord(S[0]) + k:
            for j in range(1, len(S)):
                if ord(S[j]) + k > ord('z'):
                    k1 = ord(S[j]) + k - ord('a')
                else:
                    k1 = k
                if ord(T[j]) != ord(S[j]) + k1:
                    print("No")
                    return
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()