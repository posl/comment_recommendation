def main():
    #input
    S_x,S_y,G_x,G_y = map(int,input().split())
    #calc
    ans = S_x - S_x * G_y / (G_y - S_y)
    #output
    print(ans)
