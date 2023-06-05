def sum_integers():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a))

if __name__ == '__main__':
    sum_integers()