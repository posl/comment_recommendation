def find_sum(n, s, a, b):
    if n == 1:
        if a[0] == s or b[0] == s:
            return True
        else:
            return False
    else:
        for i in range(n):
            if a[i] + b[i] == s:
                return True
            else:
                for j in range(i+1, n):
                    if a[i] + a[j] == s:
                        return True
                    if b[i] + b[j] == s:
                        return True
    return False
