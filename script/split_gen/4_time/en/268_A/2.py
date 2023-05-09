def main():
    #input
    A, B, C, D, E = map(int, input().split())
    #output
    print(len({A, B, C, D, E}))
