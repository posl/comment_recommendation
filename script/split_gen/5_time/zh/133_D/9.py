def main():
    n = int(input())
    arr = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += arr[i]
    result = []
    for i in range(n):
        result.append(sum - arr[i])
    print(' '.join(map(str, result)))
