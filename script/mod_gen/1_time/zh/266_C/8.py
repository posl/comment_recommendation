def is_convex(A, B, C, D):
    # 通过向量叉积判断两个向量的方向
    # A->B, B->C, C->D, D->A
    AB = [B[0] - A[0], B[1] - A[1]]
    BC = [C[0] - B[0], C[1] - B[1]]
    CD = [D[0] - C[0], D[1] - C[1]]
    DA = [A[0] - D[0], A[1] - D[1]]
    # 判断AB与BC的叉积方向是否相同
    if AB[0] * BC[1] - AB[1] * BC[0] < 0:
        return False
    # 判断BC与CD的叉积方向是否相同
    if BC[0] * CD[1] - BC[1] * CD[0] < 0:
        return False
    # 判断CD与DA的叉积方向是否相同
    if CD[0] * DA[1] - CD[1] * DA[0] < 0:
        return False
    # 判断DA与AB的叉积方向是否相同
    if DA[0] * AB[1] - DA[1] * AB[0] < 0:
        return False
    return True

if __name__ == '__main__':
    is_convex()