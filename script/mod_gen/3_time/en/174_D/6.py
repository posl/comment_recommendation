def main():
    N = int(input())
    stones = input()
    R = stones.count("R")
    W = stones.count("W")
    if R == 0 or W == 0:
        print(0)
        return
    if stones[0] == "R":
        R -= 1
    else:
        W -= 1
    if stones[-1] == "W":
        W -= 1
    else:
        R -= 1
    print(min(R, W))

if __name__ == '__main__':
    main()