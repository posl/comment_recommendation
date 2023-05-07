def  main():
     # Read input 
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())
     # Determine whether the given quadrilateral is convex 
    AB = (B_x - A_x) * (C_y - A_y) - (C_x - A_x) * (B_y - A_y)
    BC = (C_x - B_x) * (D_y - B_y) - (D_x - B_x) * (C_y - B_y)
    CD = (D_x - C_x) * (A_y - C_y) - (A_x - C_x) * (D_y - C_y)
    DA = (A_x - D_x) * (B_y - D_y) - (B_x - D_x) * (A_y - D_y)
    if AB * BC > 0 and BC * CD > 0 and CD * DA > 0 and DA * AB > 0:
         print ( 'Yes' )
    else:
         print ( 'No' )

if __name__ == '__main__':
    ()