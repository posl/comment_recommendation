def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i % 10 == j // (10 ** (len(str(j))-1)) and i // (10 ** (len(str(i))-1)) == j % 10:
                count += 1
    print(count)
