def roller_coaster():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in h:
        if i >= k:
            count += 1
    return count

if __name__ == '__main__':
    roller_coaster()