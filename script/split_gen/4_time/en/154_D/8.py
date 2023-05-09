def get_expected_value(n, k, p):
    expected_value = 0
    for i in range(n - k + 1):
        expected_value += (k * (k + 1) / 2) / k * sum(p[i:i + k]) / k
    return expected_value
