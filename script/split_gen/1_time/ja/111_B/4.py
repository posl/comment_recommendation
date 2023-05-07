def main():
    N = int(input())
    N = str(N)
    if N[0] == N[1] and N[1] == N[2]:
        print(N)
    else:
        if N[0] == N[1] and N[1] != N[2]:
            print(N[0]+N[1]+N[1])
        elif N[1] == N[2] and N[0] != N[1]:
            print(N[0]+N[1]+N[1])
        elif N[0] == N[2] and N[0] != N[1]:
            print(N[0]+N[1]+N[0])
        else:
            if N[0] > N[1] and N[0] > N[2]:
                print(N[0]+N[0]+N[0])
            elif N[1] > N[0] and N[1] > N[2]:
                print(N[1]+N[1]+N[1])
            elif N[2] > N[0] and N[2] > N[1]:
                print(N[2]+N[2]+N[2])
            else:
                print(N[0]+N[1]+N[2])
