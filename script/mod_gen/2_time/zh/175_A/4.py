def main():
    n = int(input())
    stones = input()
    red = stones.count('R')
    ans = 0
    for i in range(red):
        if stones[i] == 'W':
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()