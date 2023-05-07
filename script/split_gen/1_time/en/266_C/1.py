def main():
    # Write your code here
    a_x, a_y = map(int, input().split())
    b_x, b_y = map(int, input().split())
    c_x, c_y = map(int, input().split())
    d_x, d_y = map(int, input().split())
    
    #angle A
    a = (b_x - a_x) * (c_y - a_y) - (b_y - a_y) * (c_x - a_x)
    #angle B
    b = (c_x - b_x) * (d_y - b_y) - (c_y - b_y) * (d_x - b_x)
    #angle C
    c = (d_x - c_x) * (a_y - c_y) - (d_y - c_y) * (a_x - c_x)
    #angle D
    d = (a_x - d_x) * (b_y - d_y) - (a_y - d_y) * (b_x - d_x)
    
    if a > 0 and b > 0 and c > 0 and d > 0:
        print("Yes")
    elif a < 0 and b < 0 and c < 0 and d < 0:
        print("Yes")
    else:
        print("No")
