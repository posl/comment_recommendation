def main():
    S = input()
    T = input()
    ls = len(S)
    lt = len(T)
    for i in range(lt):
        if S[i] == '?':
            continue
        elif S[i] != T[i]:
            print('No')
            return
    for i in range(lt, ls):
        if S[i] == '?':
            continue
        elif S[i] != T[i-lt]:
            print('No')
            return
    print('Yes')
main()

if __name__ == '__main__':
    main()