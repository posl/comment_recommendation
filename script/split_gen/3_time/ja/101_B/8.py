def main():
    N = input()
    N = int(N)
    S = 0
    if N < 10:
        S = N
    else:
        for i in range(len(N)):
            S = S + int(N[i])
    if N % S == 0:
        print("Yes")
    else:
        print("No")
