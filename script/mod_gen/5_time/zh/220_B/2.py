def base_k_to_10(num, k):
    result = 0
    for i in range(len(num)):
        result += int(num[i]) * k**(len(num)-i-1)
    return result

if __name__ == '__main__':
    base_k_to_10()