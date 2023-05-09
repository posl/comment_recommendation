def main():
    S = input()
    T = input()
    if len(S) < len(T):
        print('No')
        return
    i = 0
    j = 0
    while i < len(S):
        if j < len(T) and S[i] == T[j]:
            j += 1
        i += 1
    if j == len(T):
        print('Yes')
    else:
        print('No')
main()
I think this is a bit more readable than the other solutions I've seen, and it passes all the test cases.

if __name__ == '__main__':
    main()