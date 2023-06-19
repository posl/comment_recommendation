def num2str(n):
    if n <= 26:
        return chr(n + 96)
    else:
        a = n // 26
        b = n % 26
        if b == 0:
            return num2str(a - 1) + num2str(26)
        else:
            return num2str(a) + num2str(b)
