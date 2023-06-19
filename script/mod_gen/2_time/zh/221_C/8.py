def main():
    N = int(input())
    A = [int(i) for i in str(N)]
    L = len(A)
    max = 0
    for i in range(2**L):
        s = []
        for j in range(L):
            if ((i >> j) & 1):
                s.append(A[j])
        if len(s) == 0 or len(s) == L:
            continue
        a = int(''.join(map(str, s)))
        b = int(''.join(map(str, list(set(A) - set(s)))))
        if a * b > max:
            max = a * b
    print(max)

if __name__ == '__main__':
    main()