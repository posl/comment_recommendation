def main():
    # Write code here
    N = int(input())
    for i in range(N+1):
        if i*4 + (N-i)*7 == N:
            print("Yes")
            break
    else:
        print("No")

if __name__ == '__main__':
    main()