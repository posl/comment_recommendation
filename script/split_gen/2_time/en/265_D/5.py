def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    #A_x + A_{x+1} + ... + A_{y-1} = P
    #A_y + A_{y+1} + ... + A_{z-1} = Q
    #A_z + A_{z+1} + ... + A_{w-1} = R
    #x < y < z < w
    #A_x + A_{x+1} + ... + A_{y-1} = P
    #A_y + A_{y+1} + ... + A_{z-1} = Q
    #A_z + A_{z+1} + ... + A_{w-1} = R
    #A_x + A_{x+1} + ... + A_{y-1} + A_y + A_{y+1} + ... + A_{z-1} + A_z + A_{z+1} + ... + A_{w-1} = P + Q + R
    #A_x + A_{x+1} + ... + A_{y-1} + A_y + A_{y+1} + ... + A_{z-1} = P + Q
    #A_z + A_{z+1} + ... + A_{w-1} = R
    #A_x + A_{x+1} + ... + A_{y-1} + A_y + A_{y+1} + ... + A_{z-1} + A_z + A_{z+1} + ... + A_{w-1} = P + Q + R
    #A_x + A_{x+1} + ... + A_{y-1} + A_y + A_{y+1} + ... + A_{z-1} + A_z + A_{z+1} + ... + A_{w-1} = P + Q + R
    #A_x + A_{x+1} + ... + A_{y-1} + A_y + A_{y+1} + ... + A_{z-1} = P + Q
    #A_x + A_{x+1} + ... + A_{y
