def main():
    N = input()
    if N[0] == N[1] == N[2]:
        print(N)
    elif N[1] == N[2]:
        print(N[0]+N[1]+N[1])
    elif N[0] == N[1]:
        print(N[0]+N[0]+N[2])
    elif N[0] == N[2]:
        print(N[0]+N[1]+N[0])
    else:
        print(N[0]+N[1]+N[2])

if __name__ == '__main__':
    main()