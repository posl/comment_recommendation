def main():
    N = int(input())
    result = 0
    for a in range(1, N):
        result += (N - 1) // a
    print(result)
