def whoWin(A,B,C):
    if C==0:
        if A>B:
            return 'Takahashi'
        else:
            return 'Aoki'
    else:
        if A>=B:
            return 'Takahashi'
        else:
            return 'Aoki'

if __name__ == '__main__':
    whoWin()