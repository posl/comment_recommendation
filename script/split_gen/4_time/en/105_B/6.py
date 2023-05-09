def main():
    N = int(input())
    for i in range(0, 25):
        for j in range(0, 15):
            if 4*i + 7*j == N:
                print("Yes")
                exit()
    print("No")
