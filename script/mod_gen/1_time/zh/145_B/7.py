def is_double_copy(N,S):
    if N%2 != 0:
        return "No"
    else:
        if S[0:N/2] == S[N/2:N]:
            return "Yes"
        else:
            return "No"

if __name__ == '__main__':
    is_double_copy()