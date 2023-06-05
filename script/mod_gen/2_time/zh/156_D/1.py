def min_power(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        mid = (arr[len(arr) / 2] + arr[len(arr) / 2 - 1]) / 2
    else:
        mid = arr[len(arr) / 2]
    power = 0
    for i in arr:
        power += (i - mid) ** 2
    return power

if __name__ == '__main__':
    min_power()