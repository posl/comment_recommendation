def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    C = [0, 0, 0, 0]
    for i in range(N):
        if S[i] == "AC":
            C[0] += 1
        elif S[i] == "WA":
            C[1] += 1
        elif S[i] == "TLE":
            C[2] += 1
        elif S[i] == "RE":
            C[3] += 1
        else:
            print("error")
    print("AC x " + str(C[0]))
    print("WA x " + str(C[1]))
    print("TLE x " + str(C[2]))
    print("RE x " + str(C[3]))
