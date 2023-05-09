def main():
    N = int(input())
    A = list(map(int, input().split()))
    #上司の人数を数える
    boss = [0] * (N+1)
    for i in range(N-1):
        boss[A[i]] += 1
    #下の人数を数える
    subordinate = [0] * (N+1)
    for i in range(N-1):
        subordinate[i+2] = boss[i+2]
        subordinate[i+2] += subordinate[A[i]]
    print(*subordinate[1:], sep='
')

if __name__ == '__main__':
    main()