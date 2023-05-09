def main():
    W, H, x, y = map(int, input().split())
    ans1 = 0
    ans2 = 0
    ans3 = 0
    ans4 = 0
    ans1 = W * H / 2
    if x == W / 2 and y == H / 2:
        ans2 = 1
    else:
        ans2 = 0
    print(ans1, ans2)

if __name__ == '__main__':
    main()