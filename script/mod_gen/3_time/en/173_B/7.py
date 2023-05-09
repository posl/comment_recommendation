def main():
    #input
    N = int(input())
    S = [input() for _ in range(N)]
    #compute
    C = [0, 0, 0, 0]
    for s in S:
        if s == "AC":
            C[0] += 1
        elif s == "WA":
            C[1] += 1
        elif s == "TLE":
            C[2] += 1
        else:
            C[3] += 1
    #output
    print("AC x " + str(C[0]))
    print("WA x " + str(C[1]))
    print("TLE x " + str(C[2]))
    print("RE x " + str(C[3]))

if __name__ == '__main__':
    main()