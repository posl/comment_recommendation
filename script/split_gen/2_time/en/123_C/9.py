def main():
    #Read input
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #Find the minimum value
    M = min(A, B, C, D, E)
    #Print output
    print((N + M - 1) // M + 4)
