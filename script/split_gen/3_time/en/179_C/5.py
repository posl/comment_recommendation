def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        for j in range(1, N//i+1):
            if i * j + j == N:
                count += 1
    print(count)
