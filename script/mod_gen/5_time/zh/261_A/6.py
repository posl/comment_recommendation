def get_line_length(l1,r1,l2,r2):
    #两个线段不相交
    if r1 <= l2 or l1 >= r2:
        return 0
    #两个线段相交
    else:
        return min(r1,r2) - max(l1,l2)

if __name__ == '__main__':
    get_line_length()