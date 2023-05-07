def main():
    N, M = map(int, input().split())
    # MをNで割った余りが0なら、最大公約数はM/N
    if M % N == 0:
        print(M // N)
        return
    # MをNで割った余りが0でないなら、最大公約数はM/Nの整数部分
    # つまり、MをNで割った商
    else:
        print(M // N)

if __name__ == '__main__':
    main()