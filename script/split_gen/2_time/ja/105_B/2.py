def main():
    N = int(input())
    for i in range(N+1):
        for j in range(N+1):
            if i*4 + j*7 == N:
                print("Yes")
                return
    print("No")
    return
