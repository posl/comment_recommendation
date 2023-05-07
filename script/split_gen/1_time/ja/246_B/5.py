def main():
    A,B = map(int,input().split())
    G = (A*A+B*B)**0.5
    print(A/G,B/G)
