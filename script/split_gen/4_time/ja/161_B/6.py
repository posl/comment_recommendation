def main():
    #n, m = list(map(int, input().split()))
    #a = list(map(int, input().split()))
    n, m = 12, 3
    a = [4, 56, 78, 901, 2, 345, 67, 890, 123, 45, 6, 789]
    print('Yes' if a[-m] >= sum(a) / (4 * m) else 'No')
