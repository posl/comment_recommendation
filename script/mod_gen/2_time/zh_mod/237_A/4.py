def is_int32(n):
    if -2**63 <= n and n < 2**63:
        return True
    else:
        return False

if __name__ == '__main__':
    is_int32()