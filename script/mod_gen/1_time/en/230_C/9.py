def main():
    N, A, B = list(map(int, input().split()))
    P, Q, R, S = list(map(int, input().split()))
    for i in range(P, Q + 1):
        row = []
        for j in range(R, S + 1):
            if (i <= A and A <= j) or (i <= N - j + 1 and N - j + 1 <= j):
                row.append('#')
            elif (i <= B and B <= j) or (i <= N - j + 1 and N - j + 1 <= j):
                row.append('#')
            else:
                row.append('.')
        print(''.join(row))
main()
Python 3.7.3 (default, May  3 2019, 17:48:47) [GCC 7.4.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> N, A, B = map(int, input().split())
1000000000000000000 999999999999999999 999999999999999999
>>> P, Q, R, S = map(int, input().split())
999999999999999998 1000000000000000000 999999999999999998 1000000000000000000
>>> np.zeros((Q - P + 1, S - R + 1), dtype=str)
array([['', '', ''],
       ['', '', ''],
       ['', '', '']], dtype='<U1')
>>> np.zeros((Q - P + 1, S - R + 1), dtype=str)
array([['', '', ''],
       ['', '', ''],
       ['', '', '']], dtype='<U1')
>>> np.zeros((Q - P + 1, S - R + 1), dtype=str)
array([['', '', ''],
       ['', '', ''],
       ['', '', '']], dtype='<U1')
>>> np.zeros((Q - P + 1, S - R + 1), dtype=str)
array([['', '', ''],
       ['', '', ''],
       ['', '', '']], dtype='<U1')
>>> np.zeros((Q - P + 1, S - R + 1), dtype=str)
array([['', '', ''],
       ['', '', ''],
       ['', '', '']],

if __name__ == '__main__':
    main()