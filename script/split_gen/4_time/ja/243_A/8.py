def shampoo(V, A, B, C):
    if V < A:
        return 'F'
    elif V < A + B:
        return 'M'
    elif V < A + B + C:
        return 'T'
