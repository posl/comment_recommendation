def main():
    N = int(input())
    cake = 4
    donuts = 7
    for i in range(N//cake+1):
        for j in range(N//donuts+1):
            if i*cake + j*donuts == N:
                print("Yes")
                return
    print("No")
