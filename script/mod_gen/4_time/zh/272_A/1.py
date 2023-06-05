def sum_of_integers():
    n = int(input())
    a = list(map(int, input().split()))
    return sum(a)

if __name__ == '__main__':
    sum_of_integers()