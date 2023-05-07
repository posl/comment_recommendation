def paint(N, A, B):
    for i in range(0, A*N):
        for j in range(0, B*N):
            if (i//A + j//B)%2 == 0:
                print(".", end="")
            else:
                print("#", end="")
        print("")

if __name__ == '__main__':
    paint()