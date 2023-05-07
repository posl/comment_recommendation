def main():
    N, A, B = map(int, input().split())
    for i in range(1, A * N + 1):
        for j in range(1, B * N + 1):
            if  ((i - 1) // A + (j - 1) // B) % 2 == 0:
                print("#", end="")
            else:
                print(".", end="")
        print()
