def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    if N % 2 == 0:
        print(sum([abs(i) for i in A]))
    else:
        print(sum([abs(i) for i in A]) - 2 * min([abs(i) for i in A if i < 0]))

if __name__ == '__main__':
    main()