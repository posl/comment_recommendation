def main():
    N = int(input())
    c = input()
    left = 0
    right = N - 1
    count = 0
    while left < right:
        if c[left] == 'W' and c[right] == 'R':
            count += 1
            left += 1
            right -= 1
        elif c[left] == 'R':
            left += 1
        elif c[right] == 'W':
            right -= 1
    print(count)
