def main():
  A_x,A_y = map(int,input().split())
  B_x,B_y = map(int,input().split())
  C_x,C_y = map(int,input().split())
  D_x,D_y = map(int,input().split())
  AB_x = B_x - A_x
  AB_y = B_y - A_y
  BC_x = C_x - B_x
  BC_y = C_y - B_y
  CD_x = D_x - C_x
  CD_y = D_y - C_y
  DA_x = A_x - D_x
  DA_y = A_y - D_y
  AB = AB_x * BC_y - AB_y * BC_x
  BC = BC_x * CD_y - BC_y * CD_x
  CD = CD_x * DA_y - CD_y * DA_x
  DA = DA_x * AB_y - DA_y * AB_x
  if AB * BC * CD * DA > 0:
    print('Yes')
  else:
    print('No')
