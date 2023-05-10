def palindrome_cost(n, a, b, s):
    is_palindrome = True
    cost = 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            is_palindrome = False
            break
    if is_palindrome:
        return 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            if s[i] == 'a' or s[n - i - 1] == 'a':
                cost += a
            else:
                cost += b
    return cost
