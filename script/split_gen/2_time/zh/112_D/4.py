def main():
    N = int(input())
    x_list = [0]*N
    y_list = [0]*N
    h_list = [0]*N
    for i in range(N):
        x_list[i],y_list[i],h_list[i] = map(int,input().split())
    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(N):
                if h_list[i] > 0:
                    H = h_list[i] + abs(x_list[i]-C_X) + abs(y_list[i]-C_Y)
                    break
            for i in range(N):
                if h_list[i] != max(H - abs(x_list[i]-C_X) - abs(y_list[i]-C_Y),0):
                    break
            else:
                print(C_X,C_Y,H)
                return
