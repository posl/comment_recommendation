def main():
    import sys
    x = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(5):
        if x[i] == 0:
            print(i+1)
            break

if __name__ == '__main__':
    main()