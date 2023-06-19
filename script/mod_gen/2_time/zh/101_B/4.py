def main():
    N = int(input())
    S = 0
    for i in str(N):
        S += int(i)
    if N % S == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()