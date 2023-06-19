def get_bit_sum(a, s):
    if a > s:
        return 'No'
    elif a == s:
        return 'Yes'
    else:
        bit_sum = 0
        while s > 0:
            bit_sum += s % 2
            s = s // 2
        if bit_sum % 2 == 0:
            return 'No'
        else:
            return 'Yes'

if __name__ == '__main__':
    get_bit_sum()