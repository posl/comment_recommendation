def find_k_str(a, b, k):
    if a == 0:
        return "b" * b
    elif b == 0:
        return "a" * a
    elif k <= 1:
        return "a" * a + "b" * b
    elif k > 2**(a + b):
        return ""
    elif k <= 2**(a + b - 1):
        return "a" + find_k_str(a - 1, b, k - 1)
    else:
        return "b" + find_k_str(a, b - 1, k - 2**(a + b - 1))
