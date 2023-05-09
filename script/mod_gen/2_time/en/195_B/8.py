def get_orange_count(A, B, W):
    W = W * 1000
    min_count = 0
    max_count = 0
    min_count = W // B
    if W % B != 0:
        min_count += 1
    max_count = W // A
    return min_count, max_count

if __name__ == '__main__':
    get_orange_count()