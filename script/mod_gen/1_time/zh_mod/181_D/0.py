def is_8mul(s):
    if len(s) == 1:
        if int(s) % 8 == 0:
            return True

if __name__ == '__main__':
    is_8mul()