def main():
    N = input()
    if len(N) == 2:
        print(int(N[0]) * int(N[1]))
    else:
        print(max(int(N[0]) * int(N[1:]), int(N[0:2]) * int(N[2:]), int(N[0:3]) * int(N[3:])))
main()
