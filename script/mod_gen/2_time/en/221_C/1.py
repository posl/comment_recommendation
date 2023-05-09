def main():
    N = int(input())
    N = str(N)
    l = len(N)
    if l == 2:
        print(int(N[0]) * int(N[1]))
    elif l == 3:
        print(max(int(N[0]) * int(N[1]) * int(N[2]), int(N[0]) * int(N[1] + N[2]), int(N[0] + N[1]) * int(N[2])))
    else:
        print(max(int(N[0]) * int(N[1]) * int(N[2]) * int(N[3]), int(N[0]) * int(N[1]) * int(N[2] + N[3]), int(N[0]) * int(N[1] + N[2]) * int(N[3]), int(N[0] + N[1]) * int(N[2]) * int(N[3]), int(N[0]) * int(N[1] + N[2] + N[3]), int(N[0] + N[1]) * int(N[2] + N[3]), int(N[0] + N[1] + N[2]) * int(N[3])))

if __name__ == '__main__':
    main()