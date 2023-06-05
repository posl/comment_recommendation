def judge(S):
    for i in range(1, len(S)):
        if len(S)%i == 0:
            if S[0:i]*(len(S)//i) == S:
                return True
    return False
