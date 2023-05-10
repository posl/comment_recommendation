def problem190_a():
    # Get input
    A, B, C = map(int, input().split())
    # Solve
    if C == 0:
        A -= 1
        if A >= B:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        B -= 1
        if B >= A:
            print('Aoki')
        else:
            print('Takahashi')

if __name__ == '__main__':
    problem190_a()