def main():
    K = int(input())
    print("".join([chr(ord("A") + i) for i in range(K)]))

if __name__ == '__main__':
    main()