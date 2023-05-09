def main():
    S = input()
    T = input()
    S = S + ' '
    T = T + ' '
    s = 0
    t = 0
    while s < len(S) - 1 and t < len(T) - 1:
        if S[s] == T[t]:
            s += 1
            t += 1
        elif S[s + 1] == T[t]:
            s += 1
        elif S[s] == T[t + 1]:
            t += 1
        else:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()