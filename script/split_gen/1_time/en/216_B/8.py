def main():
    N = int(input())
    ST = [input().split() for _ in range(N)]
    ST.sort()
    for i in range(N-1):
        if ST[i][0] == ST[i+1][0] and ST[i][1] == ST[i+1][1]:
            print('Yes')
            break
    else:
        print('No')
