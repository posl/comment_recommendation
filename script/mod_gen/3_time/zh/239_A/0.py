def horizon(H):
    if H < 1 or H > 10**5:
        return None
    return (H*(12800000+H))**0.5

if __name__ == '__main__':
    horizon()