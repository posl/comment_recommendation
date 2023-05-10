def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(1/sum([1/i for i in A]))

if __name__ == '__main__':
    main()