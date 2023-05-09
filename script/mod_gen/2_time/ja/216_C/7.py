def main():
    N = int(input())
    S = []
    while N > 0:
        if N % 2 == 0:
            N = N // 2
            S.append('B')
        else:
            N -= 1
            S.append('A')
    S.reverse()
    print(''.join(S))

if __name__ == '__main__':
    main()