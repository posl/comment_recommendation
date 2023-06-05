def and_or(n,s):
    if n == 1:
        if s[0] == "AND":
            return 2
        else:
            return 1
    if s[n-1] == "AND":
        return and_or(n-1,s) * 2
    else:
        return and_or(n-1,s) + 1

if __name__ == '__main__':
    and_or()