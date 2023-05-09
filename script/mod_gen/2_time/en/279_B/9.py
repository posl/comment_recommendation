def check_substring(S, T):
    if len(S) < len(T):
        return "No"
    if S == T:
        return "Yes"
    for i in range(len(S) - len(T) + 1):
        if S[i:i + len(T)] == T:
            return "Yes"
    return "No"

if __name__ == '__main__':
    check_substring()