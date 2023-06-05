def main():
    N = int(input())
    count = 0
    for i in range(1, N):
        for j in range(i, N):
            if i * j < N:
                count += 1
            else:
                break
    print(count)
