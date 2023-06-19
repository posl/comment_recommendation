def main():
    line = input().split()
    D = int(line[0])
    T = int(line[1])
    S = int(line[2])
    if D % S == 0:
        if D / S <= T:
            print("Yes")
        else:
            print("No")
    else:
        if D / S < T:
            print("Yes")
        else:
            print("No")
