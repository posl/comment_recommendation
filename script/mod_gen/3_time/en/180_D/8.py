def main():
    X, Y, A, B = map(int, input().split())
    #X: initial strength
    #Y: maximum strength
    #A: multiplier for Kakomon Gym
    #B: increment for AtCoder Gym
    if A * X >= Y:
        print(0)
        return
    n = 0
    while A * X <= Y - B:
        X *= A
        n += 1
    print(n + (Y - 1 - X) // B)

if __name__ == '__main__':
    main()