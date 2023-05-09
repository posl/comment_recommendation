def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    result = []
    for i in range(P, Q+1):
        row = ''
        for j in range(R, S+1):
            if (i-j) % 2 == 0:
                row += '.'
            else:
                row += '#'
        result.append(row)
    print('\n'.join(result))

if __name__ == '__main__':
    main()