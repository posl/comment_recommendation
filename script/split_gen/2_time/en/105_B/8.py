def main():
    N = int(input())
    for i in range(1, 100):
        for j in range(1, 100):
            if i * 4 + j * 7 == N:
                print("Yes")
                return
    print("No")
main()
