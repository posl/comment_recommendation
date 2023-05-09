def main():
    S = input()
    S = S[::-1]
    for i in range(len(S)):
        if S[i] == 'a':
            continue
        else:
            S = S[:i] + 'a' + S[i:]
            break
    if S == S[::-1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()