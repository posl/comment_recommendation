def main():
    N = int(input())
    cnt = 0
    for i in range(1, int(N**0.5)+1):
        for j in range(i, int((N/i)**0.5)+1):
            if i == j:
                cnt += 1
            else:
                cnt += 3
    print(cnt)
