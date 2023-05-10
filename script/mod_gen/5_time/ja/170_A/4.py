def main():
    x = input().split()
    for i in range(len(x)):
        if int(x[i]) == 0:
            print(i+1)

if __name__ == '__main__':
    main()