def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(sum([i % 2 for i in A]))

if __name__ == '__main__':
    main()