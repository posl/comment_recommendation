def main():
    x = input().split(" ")
    for i in range(5):
        if x[i] == "0":
            print(i+1)
            return

if __name__ == '__main__':
    main()