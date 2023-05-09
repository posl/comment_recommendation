def main():
    N = int(input())
    x_list = list(map(int, input().split()))
    x_list_abs = [abs(x) for x in x_list]
    print(sum(x_list_abs))
    print(sum([x**2 for x in x_list_abs])**(1/2))
    print(max(x_list_abs))

if __name__ == '__main__':
    main()