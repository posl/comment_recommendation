def prefix(S, T):
    if S == T[:len(S)]:
        return "Yes"
    return "No"

if __name__ == '__main__':
    prefix()