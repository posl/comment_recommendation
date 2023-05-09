def getComplement(b):
    if b == 'A':
        return 'T'
    elif b == 'T':
        return 'A'
    elif b == 'C':
        return 'G'
    elif b == 'G':
        return 'C'
    else:
        return 'ERROR'

if __name__ == '__main__':
    getComplement()