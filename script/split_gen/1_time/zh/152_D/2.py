def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        for j in range(i, N+1):
            if i%10 == j//100 and j%10 == i//100:
                cnt += 2
                if i == j:
                    cnt -= 1
    print(cnt)
