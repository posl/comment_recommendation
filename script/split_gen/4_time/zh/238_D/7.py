def get_bit_sum(a, s):
    if s > a:
        return "No"
    else:
        if s == a:
            return "Yes"
        else:
            if s % 2 == 0:
                if a % 2 == 0:
                    return "Yes"
                else:
                    return "No"
            else:
                if a % 2 == 0:
                    return "No"
                else:
                    return "Yes"
