def sum_of_ints():
    n = int(input())
    a = list(map(int, input().split()))
    ans = sum(a)
    print(ans)
    return
sum_of_ints()

if __name__ == '__main__':
    sum_of_ints()