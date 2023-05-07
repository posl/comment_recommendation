def main():
    S = input()
    K = int(input())
    S = S.replace(".", "X")
    if K == 0:
        print(S.count("X"))
        return
    if K >= len(S):
        print(len(S))
        return
    for i in range(len(S)):
        if S[i] == "X":
            S = S[:i] + "." + S[i + 1:]
            break
    for i in range(len(S) - 1, -1, -1):
        if S[i] == "X":
            S = S[:i] + "." + S[i + 1:]
            break
    print(S.count("X") + 1)

if __name__ == '__main__':
    main()