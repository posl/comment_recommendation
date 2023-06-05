def main():
    K = int(input())
    print("".join([chr(i) for i in range(ord('A'), ord('A')+K)]))

if __name__ == '__main__':
    main()