def get_complement_base(base):
    if base == 'A':
        return 'T'
    elif base == 'C':
        return 'G'
    elif base == 'G':
        return 'C'
    elif base == 'T':
        return 'A'
    else:
        return ''
