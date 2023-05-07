def main():
    N = int(input())
    for i in range(2**15):
        if N & i == i:
            print(i)

if __name__ == '__main__':
    main()