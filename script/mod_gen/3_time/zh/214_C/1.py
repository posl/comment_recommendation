def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    for i in range(N):
        if i == 0:
            time = T[i]
            continue
        else:
            if time > T[i]:
                time = T[i]
            else:
                pass
        time += S[i]
        print(time)

if __name__ == '__main__':
    main()