def main():
    s = input()
    for i in range(1,10):
        if s.find(str(i)) == -1:
            print(i)
            break

if __name__ == '__main__':
    main()