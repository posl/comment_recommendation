def main():
    N = int(input())
    total = 0
    for i in range(1, N):
        total += i
        if total >= N:
            print(i)
            break
main()
