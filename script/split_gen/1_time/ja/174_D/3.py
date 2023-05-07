def main():
    N = int(input())
    c = input()
    R = c.count("R")
    W = c.count("W")
    print(min(R, W))
