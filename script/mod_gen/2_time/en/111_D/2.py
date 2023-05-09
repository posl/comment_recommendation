def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    m = 40
    d = [1] * m
    for i in range(m - 1):
        d[i + 1] = d[i] * 2
    d.reverse()
    print(m)
    print(*d)
    for i in range(n):
        ans = ""
        for j in range(m):
            if (x[i] & 1) == 1 and (y[i] & 1) == 1:
                ans += "RU"
                x[i] -= 1
                y[i] -= 1
            elif (x[i] & 1) == 1 and (y[i] & 1) == 0:
                ans += "RD"
                x[i] -= 1
                y[i] += 1
            elif (x[i] & 1) == 0 and (y[i] & 1) == 1:
                ans += "LU"
                x[i] += 1
                y[i] -= 1
            elif (x[i] & 1) == 0 and (y[i] & 1) == 0:
                ans += "LD"
                x[i] += 1
                y[i] += 1
            x[i] >>= 1
            y[i] >>= 1
        print(ans)
main()
I tried to solve this problem by myself, but I couldn't.
So, I saw the editorial and tried to understand it.
I have a question.
In the editorial, it says that the distance from (x, y) to (x', y') is |x - x'| + |y - y'|.
But, I think the distance from (x, y) to (x', y') is max(|x - x'|, |y - y'|).
Is my understanding wrong?
Thank you.
I think you are correct. I think it's a typo in the editorial.
Thank you for your reply.
I'm glad to hear that.
I have another question.
In the editorial, it says that the distance from (x, y) to (x', y') is |x - x'|

if __name__ == '__main__':
    main()