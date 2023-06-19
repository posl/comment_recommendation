def make_sequence(n, s):
    if n == 1:
        if s >= 3:
            return 1
        else:
            return 0
    else:
        count = 0
        for i in range(3, s+1):
            count += make_sequence(n-1, s-i)
        return count

if __name__ == '__main__':
    make_sequence()