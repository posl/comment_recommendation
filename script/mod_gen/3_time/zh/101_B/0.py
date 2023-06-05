def main():
    N = int(input())
    sum = 0
    for i in str(N):
        sum += int(i)
    if N % sum == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()