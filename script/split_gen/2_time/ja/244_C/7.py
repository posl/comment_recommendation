def main():
    N = int(input())
    for i in range(1, N+1):
        print(i)
        a = int(input())
        if a == 0:
            break
    print(2*N+1)
