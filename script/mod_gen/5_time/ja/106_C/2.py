def main():
    S = input()
    K = int(input())
    print(S[(K-1)%len(S)])

if __name__ == '__main__':
    main()