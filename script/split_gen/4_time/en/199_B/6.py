def problem199_b():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_max = max(a)
    b_min = min(b)
    if b_min < a_max:
        print(0)
    else:
        print(b_min - a_max + 1)
