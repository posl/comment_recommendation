def main():
    #N = int(input())
    N = 11
    for i in range(0, N):
        for j in range(0, N):
            if (4*i + 7*j == N):
                print("Yes")
                return
    print("No")
