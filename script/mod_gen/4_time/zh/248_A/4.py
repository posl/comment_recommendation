def main():
    str = input()
    for i in range(1,10):
        if str.find(str(i)) == -1:
            print(i)
            break

if __name__ == '__main__':
    main()