def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    temp = [T - H_i * 0.006 for H_i in H]
    dist = [abs(A - temp_i) for temp_i in temp]
    print(dist.index(min(dist)) + 1)

if __name__ == '__main__':
    main()