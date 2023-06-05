def main():
    N = int(input())
    s = 0
    for i in range(1, N+1):
        s += i
        if s >= N:
            break
    if s == N:
        print(i)
        exit()
    else:
        print(i-1)
        exit()
