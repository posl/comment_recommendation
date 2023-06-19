def main():
    # S = input()
    # T = input()
    S = 'CSS'
    T = 'CSR'
    n = 0
    for i in range(3):
        if S[i] == T[i]:
            n += 1
    print(n)

if __name__ == '__main__':
    main()