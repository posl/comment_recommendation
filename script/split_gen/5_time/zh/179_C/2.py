def main():
    N = int(input())
    count = 0
    for i in range(1,N):
        if N % i == 0:
            if i == N/i:
                count += 1
            else:
                count += 2
    print(count)
