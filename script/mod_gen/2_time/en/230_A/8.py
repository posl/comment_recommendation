def AGC(N):
    if N < 43:
        return "AGC" + str(N).zfill(3)
    else:
        return "AGC" + str(N+1).zfill(3)
N = int(input())
print(AGC(N))

if __name__ == '__main__':
    AGC()