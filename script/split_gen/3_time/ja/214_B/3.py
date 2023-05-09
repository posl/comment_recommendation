def main():
    S, T = map(int, input().split())
    cnt = 0
    for i in range(S+1):
        for j in range(S+1):
            for k in range(S+1):
                if i+j+k <= S and i*j*k <= T:
                    cnt += 1
    print(cnt)
