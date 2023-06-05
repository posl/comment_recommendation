def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        query = input()
        if query == '1':
            S = S[::-1]
        else:
            T_i, F_i, C_i = query.split()
            if F_i == '1':
                S = C_i + S
            else:
                S = S + C_i
    print(S)

if __name__ == '__main__':
    main()