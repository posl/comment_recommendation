def search(possible, target, total, n):
    if total == target:
        return 1
    elif total > target or n == len(possible):
        return 0
    else:
        return search(possible, target, total + possible[n], n + 1) + search(possible, target, total, n + 1)
