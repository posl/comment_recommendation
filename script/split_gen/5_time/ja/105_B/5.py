def main():
    n = int(input())
    for i in range(0, n//4 + 1):
        for j in range(0, n//7 + 1):
            if i*4 + j*7 == n:
                print("Yes")
                exit()
    print("No")
