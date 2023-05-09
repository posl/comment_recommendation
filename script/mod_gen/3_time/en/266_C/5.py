def is_convex(A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y):
    
    def cross_product(x1,y1,x2,y2):
        return x1*y2-x2*y1
    
    #calculate the cross product of the vectors AB and AD
    AB_AD=cross_product(B_x-A_x,B_y-A_y,D_x-A_x,D_y-A_y)
    #calculate the cross product of the vectors AB and AC
    AB_AC=cross_product(B_x-A_x,B_y-A_y,C_x-A_x,C_y-A_y)
    #calculate the cross product of the vectors BC and BD
    BC_BD=cross_product(C_x-B_x,C_y-B_y,D_x-B_x,D_y-B_y)
    #calculate the cross product of the vectors BC and BA
    BC_BA=cross_product(C_x-B_x,C_y-B_y,A_x-B_x,A_y-B_y)
    #calculate the cross product of the vectors CD and CA
    CD_CA=cross_product(D_x-C_x,D_y-C_y,A_x-C_x,A_y-C_y)
    #calculate the cross product of the vectors CD and CB
    CD_CB=cross_product(D_x-C_x,D_y-C_y,B_x-C_x,B_y-C_y)
    #calculate the cross product of the vectors DA and DB
    DA_DB=cross_product(A_x-D_x,A_y-D_y,B_x-D_x,B_y-D_y)
    #calculate the cross product of the vectors DA and DC
    DA_DC=cross_product(A_x-D_x,A_y-D_y,C_x-D_x,C_y-D_y)
    
    #if the cross product is positive, return True
    if AB_AD>=0 and AB_AC>=0 and BC_BD>=0 and BC_BA>=0 and CD_CA>=0 and CD_CB>=0 and DA_DB>=0 and DA_DC>=0:
        return True
    #if the cross product is negative, return False
    elif AB_AD<=0 and AB_AC<=0 and BC_BD<=0 and BC_BA<=0 and CD_CA<=0 and CD_CB<=0 and DA_DB<=0 and DA_DC<=0:
        return False
    #if the cross product is 0, return None
    else:
        return None

if __name__ == '__main__':
    is_convex()