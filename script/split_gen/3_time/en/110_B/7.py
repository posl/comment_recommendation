def main():
    # input
    NMXY = input()
    NMXY = NMXY.split(" ")
    N = int(NMXY[0])
    M = int(NMXY[1])
    X = int(NMXY[2])
    Y = int(NMXY[3])
    x = input()
    x = x.split(" ")
    x = list(map(int, x))
    y = input()
    y = y.split(" ")
    y = list(map(int, y))
    
    # process
    war = "No War"
    x_max = max(x)
    y_min = min(y)
    for z in range(X+1, Y+1):
        if x_max < z and z <= y_min:
            war = "War"
            break
    
    # output
    print(war)
