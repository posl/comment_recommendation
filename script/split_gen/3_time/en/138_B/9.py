def problem138_b():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum(1 / i for i in a))
