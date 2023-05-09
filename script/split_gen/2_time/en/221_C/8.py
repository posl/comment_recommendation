def main():
    #input
    N = input()
    #compute
    #output
    print(max(int(N[:-1]) * int(N[-1]), int(N[0]) * int(N[1:])))
