def main():
    N = int(input())
    if N == 1:
        print("No")
        return
    for i in range(1, 10):
        if N % i == 0:
            if N // i >= 1 and N // i <= 9:
                print("Yes")
                return
    print("No")
    return
main()
