def main():
    # N = int(input())
    N = 963761198400
    # N = 12
    count = 0
    for i in range(1, N+1):
        sum = 0
        for j in range(i, N+1):
            sum += j
            if sum == N:
                count += 1
                break
            elif sum > N:
                break
    print(count)
