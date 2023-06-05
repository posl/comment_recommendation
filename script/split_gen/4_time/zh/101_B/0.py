def problem101_b(N):
    if N < 1 or N > 10**9:
        return "No"
    sum = 0
    num = N
    while num > 0:
        sum += num % 10
        num //= 10
    if sum % N == 0:
        return "Yes"
    else:
        return "No"
