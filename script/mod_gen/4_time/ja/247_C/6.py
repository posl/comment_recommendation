def main():
    N = int(input())
    S = [1]
    for i in range(2,N+1):
        S = S + [i] + S
    print(' '.join(map(str,S)))

if __name__ == '__main__':
    main()