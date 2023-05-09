def main():
    N = input()
    N = int(N)
    S = 0
    for i in range(len(str(N))):
        S += int(str(N)[i])
    if N % S == 0:
        print("Yes")
    else:
        print("No")
