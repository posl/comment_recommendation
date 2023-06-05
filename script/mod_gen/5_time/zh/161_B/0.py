def isPopular(items, m):
    total = sum(items)
    for item in items:
        if item < total/(4*m):
            return False
    return True

if __name__ == '__main__':
    isPopular()