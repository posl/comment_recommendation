def main():
    N = int(input())
    x = 0
    for i in range(1, N+1):
        x += i
        if x >= N:
            print(i)
            break
