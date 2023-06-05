def is_same_line(p1,p2,p3):
    if p1[0] == p2[0] and p1[0] == p3[0]:
        return True
    if p1[0] == p2[0] or p1[0] == p3[0]:
        return False
    a1 = (p2[1]-p1[1])/(p2[0]-p1[0])
    a2 = (p3[1]-p1[1])/(p3[0]-p1[0])
    if a1 == a2:
        return True
    return False

if __name__ == '__main__':
    is_same_line()