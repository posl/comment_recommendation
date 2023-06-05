def get_good_choice(N, a):
    if N == 1:
        if a[0] == 1:
            return [1]
        else:
            return []
    if N == 2:
        if a[0] == a[1]:
            if a[0] == 0:
                return []
            else:
                return [1]
        else:
            return []
    if N == 3:
        if a[0] == a[1] and a[1] == a[2]:
            if a[0] == 0:
                return []
            else:
                return [1]
        else:
            return []
    if N % 2 == 0:
        if a[0] == a[N - 1]:
            if a[0] == 0:
                return []
            else:
                return [1]
        else:
            return []
    else:
        if a[0] == a[N - 1]:
            if a[0] == 0:
                return []
            else:
                return [1]
        else:
            return []
N = int(input())
a = list(map(int, input().split()))
choice = get_good_choice(N, a)
