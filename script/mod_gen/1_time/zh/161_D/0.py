def is_llsk(n):
    s = str(n)
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i-1])) > 1:
            return False
    return True

if __name__ == '__main__':
    is_llsk()