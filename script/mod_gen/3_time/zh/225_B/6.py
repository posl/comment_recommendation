def check_star(n, edge):
    #print(n, edge)
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 0:
        return False
    if edge[0][0] == edge[1][0]:
        return True
    if edge[0][0] == edge[1][1]:
        return True
    if edge[0][1] == edge[1][0]:
        return True
    if edge[0][1] == edge[1][1]:
        return True
    return False

if __name__ == '__main__':
    check_star()