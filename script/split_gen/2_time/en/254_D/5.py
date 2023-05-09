def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j <= N:
                if i == j:
                    count += 1
                elif i*j == i*i or i*j == j*j:
                    count += 2
    print(count)
