def main():
    N = int(input())
    for i in range(0,N+1):
        for j in range(0,N+1):
            if i*4 + j*7 == N:
                print("Yes")
                return
    print("No")
    return
