def is_approved(ary):
    for i in ary:
        if i % 2 == 0 and (i % 3 != 0 and i % 5 != 0):
            return False
    return True

if __name__ == '__main__':
    is_approved()