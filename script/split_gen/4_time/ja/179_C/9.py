def main():
    N = int(input())
    result = 0
    for i in range(1, N):
        for j in range(1, N):
            if N - j * i <= 0:
                break
            result += 1
    print(result)
