def main():
    #input
    X = int(input())
    #compute
    for A in range(-118,120):
        for B in range(-119,119):
            if A**5 - B**5 == X:
                #output
                print(A,B)
                exit()
