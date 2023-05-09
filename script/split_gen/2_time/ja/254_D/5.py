def main():
    N = int(input())
    cnt = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if (i*j)**0.5 == int((i*j)**0.5):
                cnt += 1
    print(cnt)
