def Takahashi_or_Aoki(A,B,C):
    if C == 0:
        if A > B:
            return 'Takahashi'
        else:
            return 'Aoki'
    else:
        if A > B:
            return 'Aoki'
        else:
            return 'Takahashi'
