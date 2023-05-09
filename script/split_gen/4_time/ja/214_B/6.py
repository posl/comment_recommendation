def main():
    s,t = map(int,input().split())
    cnt = 0
    for i in range(s+1):
        for j in range(s+1):
            for k in range(s+1):
                if i + j + k <= s and i * j * k <= t:
                    cnt += 1
    print(cnt)
