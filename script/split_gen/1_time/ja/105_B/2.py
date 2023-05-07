def main():
    N = int(input())
    for i in range(0, N+1, 4):
        for j in range(0, N+1, 7):
            if i+j == N:
                print("Yes")
                return
    print("No")
    return
