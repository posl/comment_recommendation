def is_substring(S: str) -> str:
    T = 'oxx' * 10**5
    if S in T:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    is_substring()