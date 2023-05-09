def problem222_b():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([i for i in a if i < p]))

if __name__ == '__main__':
    problem222_b()