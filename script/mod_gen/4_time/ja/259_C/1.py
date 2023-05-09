def main():
    S = input()
    T = input()
    i = 0
    j = 0
    while i < len(S) and j < len(T):
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == len(S):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()