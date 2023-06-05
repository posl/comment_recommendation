def get_second_smallest_number(p):
    if p[0] < p[1]:
        if p[1] < p[2]:
            return p[1]
        else:
            return p[2]
    else:
        if p[0] < p[2]:
            return p[0]
        else:
            return p[2]

if __name__ == '__main__':
    get_second_smallest_number()