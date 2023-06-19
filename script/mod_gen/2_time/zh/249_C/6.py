def is_included(Si, Sj):
    for c in Si:
        if c in Sj:
            return True
    return False

if __name__ == '__main__':
    is_included()