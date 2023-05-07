def main():
    N = int(input())
    S = input()
    R = S.count("R")
    W = S.count("W")
    print(min(R, W))
