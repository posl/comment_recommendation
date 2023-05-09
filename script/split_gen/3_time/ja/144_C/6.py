def main():
    N = int(input())
    if N == 2:
        print(1)
        return
    elif N == 3:
        print(2)
        return
    else:
        m = 0
        for i in range(1, N):
            if i * i <= N:
                m = i
            else:
                break
        print(N - m)
