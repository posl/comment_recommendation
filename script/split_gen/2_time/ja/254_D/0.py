def main():
    N = int(input())
    count = 0
    for i in range(1, int(N**0.5)+1):
        for j in range(1, int(N**0.5)+1):
            if i*j <= N:
                count += 1
    print(count)
