def problem258_a():
    k = int(input())
    h = k // 60
    m = k % 60
    print(f'{21 + h:02}:{m:02}')
