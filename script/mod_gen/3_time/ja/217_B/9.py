def main():
    S = [input() for _ in range(3)]
    print(*set('ABC')-set(S), sep='')

if __name__ == '__main__':
    main()