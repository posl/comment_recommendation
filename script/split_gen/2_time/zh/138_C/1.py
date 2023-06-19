def main():
    N = int(input())
    values = list(map(int, input().split()))
    values.sort()
    result = values[0]
    for i in range(1, N):
        result = (result + values[i]) / 2
    print(result)
