def main():
    #input
    a,b,c = map(int, input().split())
    #compute
    if c == 0:
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if a >= b:
            print("Takahashi")
        else:
            print("Aoki")
    #output
