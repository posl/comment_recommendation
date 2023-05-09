def can_see_ocean(h):
    max_height = 0
    for i in h:
        if i >= max_height:
            max_height = i
        else:
            return False
    return True

if __name__ == '__main__':
    can_see_ocean()