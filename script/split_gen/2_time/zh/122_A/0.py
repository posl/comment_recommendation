def get_complementary_base(input_base):
    if input_base == 'A':
        return 'T'
    elif input_base == 'C':
        return 'G'
    elif input_base == 'G':
        return 'C'
    elif input_base == 'T':
        return 'A'
    else:
        return ''
