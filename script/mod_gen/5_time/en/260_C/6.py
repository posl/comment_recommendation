def get_jewel_count(N, X, Y):
    if X > Y:
        return 0
    else:
        return (N-1)*X + Y

if __name__ == '__main__':
    get_jewel_count()