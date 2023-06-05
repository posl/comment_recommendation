def is_wonderful_string(S):
    if S[0].isupper() and S[1].islower():
        for i in range(2,len(S),2):
            if S[i].isupper() or S[i+1].islower():
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    is_wonderful_string()