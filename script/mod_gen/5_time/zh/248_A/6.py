def main():
    a = input()
    a = list(a)
    b = [str(i) for i in range(10)]
    for i in b:
        if i not in a:
            print(i)
            break

if __name__ == '__main__':
    main()