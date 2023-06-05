def main():
    #读取四个坐标点
    A_x,A_y = map(int,input().split())
    B_x,B_y = map(int,input().split())
    C_x,C_y = map(int,input().split())
    D_x,D_y = map(int,input().split())
    #计算向量AB和向量BC的叉积
    AB_x = B_x - A_x
    AB_y = B_y - A_y
    BC_x = C_x - B_x
    BC_y = C_y - B_y
    AB_BC = AB_x * BC_y - AB_y * BC_x
    #计算向量BC和向量CD的叉积
    CD_x = D_x - C_x
    CD_y = D_y - C_y
    BC_CD = BC_x * CD_y - BC_y * CD_x
    #计算向量CD和向量DA的叉积
    DA_x = A_x - D_x
    DA_y = A_y - D_y
    CD_DA = CD_x * DA_y - CD_y * DA_x
    #计算向量DA和向量AB的叉积
    AB_DA = AB_x * DA_y - AB_y * DA_x
    if AB_BC * BC_CD > 0 and BC_CD * CD_DA > 0 and CD_DA * AB_DA > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()