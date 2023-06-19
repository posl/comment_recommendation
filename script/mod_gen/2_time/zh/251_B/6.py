def func(n,w,weights):
    weights.sort()
    n = min(n,3)
    if n == 1:
        return 1 if weights[0] <= w else 0
    elif n == 2:
        return 1 if weights[0] + weights[1] <= w else 0
    elif n == 3:
        return 1 if weights[0] + weights[1] <= w else 0 + 1 if weights[0] + weights[2] <= w else 0 + 1 if weights[1] + weights[2] <= w else 0 + 1 if weights[0] + weights[1] + weights[2] <= w else 0
    else:
        return 0

if __name__ == '__main__':
    func()