def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab = sorted(ab, key=lambda x:x[0]+x[1], reverse=True)
    a_sum = 0
    b_sum = 0
    for i in range(n):
        a_sum += ab[i][0]
    ans = 0
    for i in range(n):
        a_sum -= ab[i][0]
        b_sum += ab[i][0]+ab[i][1]
        ans += 1
        if a_sum < b_sum:
            break
    print(ans)

if __name__ == '__main__':
    main()