def main():
    S = input()
    if S[0] == '1':
        print('No')
        return
    split = False
    for i in range(1, len(S)):
        if S[i] == '1':
            if S[i-1] == '0':
                split = True
                break
    if split:
        print('Yes')
    else:
        print('No')
main()

if __name__ == '__main__':
    main()