def main():
    N = int(input())
    count = 1
    for i in range(1, N):
        if i % 2 == 0:
            count += 1
    print(count)
