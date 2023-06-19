def is_included(Si, Sj):
    for c in Si:
        if c in Sj:
            return True
    return False
