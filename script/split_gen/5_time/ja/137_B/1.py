def main():
    k, x = map(int, input().split())
    result = []
    for i in range(x-k+1, x+k):
        result.append(i)
    print(*result)
