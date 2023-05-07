def nuts(nuts):
    total = 0
    for n in nuts:
        if n > 10:
            total += n-10
    return total

if __name__ == '__main__':
    nuts()