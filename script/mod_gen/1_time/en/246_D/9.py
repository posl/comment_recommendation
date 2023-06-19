def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    i = 0
    while True:
        i += 1
        if N <= i**3:
            break
    print(i**3)
main()
