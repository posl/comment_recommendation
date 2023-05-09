def main():
    S = input()
    T = input()
    s = 0
    t = 0
    while t < len(T):
        if s < len(S) and S[s] == T[t]:
            s += 1
            t += 1
        elif t > 0 and T[t] == T[t - 1]:
            t += 1
        else:
            print('No')
            return
    if s == len(S):
        print('Yes')
    else:
        print('No')
main()

if __name__ == '__main__':
    main()