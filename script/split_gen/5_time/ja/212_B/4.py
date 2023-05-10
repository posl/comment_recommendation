def main():
    N = input()
    if N[0] == N[1] == N[2] == N[3]:
        print("Weak")
    else:
        if (int(N[0])+1)%10 == int(N[1]) and (int(N[1])+1)%10 == int(N[2]) and (int(N[2])+1)%10 == int(N[3]):
            print("Weak")
        else:
            print("Strong")
