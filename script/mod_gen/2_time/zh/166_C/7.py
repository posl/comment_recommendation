def is_higher(h, i):
    for j in range(len(h)):
        if h[j] > h[i]:
            return False
    return True

if __name__ == '__main__':
    is_higher()