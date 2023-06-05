def main():
    #input
    x = list(map(int, input().split()))
    #search
    for i in range(5):
        if x[i] == 0:
            print(i+1)
            break

if __name__ == '__main__':
    main()