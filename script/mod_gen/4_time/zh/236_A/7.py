def problem236_a():
    s = input()
    a,b = map(int, input().split())
    lst = list(s)
    lst[a-1], lst[b-1] = lst[b-1], lst[a-1]
    print(''.join(lst))

if __name__ == '__main__':
    problem236_a()