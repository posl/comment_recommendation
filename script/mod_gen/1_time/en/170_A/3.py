def main():
    x = input().split()
    for i in range(len(x)):
        if x[i] == '0':
            print(i+1)
            break
main()

if __name__ == '__main__':
    main()