def main():
    k = int(input())
    print("".join([chr(i) for i in range(ord("A"), ord("A") + k)]))

if __name__ == '__main__':
    main()