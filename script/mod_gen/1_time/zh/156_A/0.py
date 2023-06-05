def get_intrinsic_evaluation(n,r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)

if __name__ == '__main__':
    get_intrinsic_evaluation()