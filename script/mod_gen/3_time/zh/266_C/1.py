def is_convex(A,B,C,D):
    if cross_product(A,B,C)*cross_product(B,C,D)<0:
        return False
    if cross_product(B,C,D)*cross_product(C,D,A)<0:
        return False
    if cross_product(C,D,A)*cross_product(D,A,B)<0:
        return False
    if cross_product(D,A,B)*cross_product(A,B,C)<0:
        return False
    return True

if __name__ == '__main__':
    is_convex()