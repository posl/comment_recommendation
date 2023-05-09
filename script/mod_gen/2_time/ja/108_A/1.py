def main():
    k = int(input())
    even = [i for i in range(1, k + 1) if i % 2 == 0]
    odd = [i for i in range(1, k + 1) if i % 2 == 1]
    print(len(even) * len(odd))

if __name__ == '__main__':
    main()