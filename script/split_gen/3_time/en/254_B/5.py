def main():
    N = int(input())
    for i in range(N):
        s = [1]
        for j in range(i):
            s.append(s[-1] * (i-j) // (j+1))
        print(*s)
