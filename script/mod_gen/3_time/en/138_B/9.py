def problem138_b():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum(1 / i for i in a))

if __name__ == '__main__':
    problem138_b()