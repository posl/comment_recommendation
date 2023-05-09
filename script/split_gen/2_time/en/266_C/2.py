def main():
    # A_x A_y
    # B_x B_y
    # C_x C_y
    # D_x D_y
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())
    #print(A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y)
    # A -> B -> C -> D -> A
    # A -> C -> B -> D -> A
    # A -> B -> D -> C -> A
    # A -> D -> B -> C -> A
    # A -> C -> D -> B -> A
    # A -> D -> C -> B -> A
    if isConvex(A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y) or \
       isConvex(A_x, A_y, C_x, C_y, B_x, B_y, D_x, D_y) or \
       isConvex(A_x, A_y, B_x, B_y, D_x, D_y, C_x, C_y) or \
       isConvex(A_x, A_y, D_x, D_y, B_x, B_y, C_x, C_y) or \
       isConvex(A_x, A_y, C_x, C_y, D_x, D_y, B_x, B_y) or \
       isConvex(A_x, A_y, D_x, D_y, C_x, C_y, B_x, B_y):
        print("Yes")
    else:
        print("No")
