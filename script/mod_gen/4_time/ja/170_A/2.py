def main():
    x = list(map(int, input().split()))
    for i in range(len(x)):
        if x[i] == 0:
            print(i+1)
            return

if __name__ == '__main__':
    main()