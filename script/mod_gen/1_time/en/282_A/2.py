def main():
    k = int(input())
    print("".join([chr(i) for i in range(65, 65 + k)]))

if __name__ == '__main__':
    main()