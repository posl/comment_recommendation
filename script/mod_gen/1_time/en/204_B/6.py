def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum([a-10 if a>10 else 0 for a in A]))

if __name__ == '__main__':
    main()