def main():
    n = int(input())
    x = []
    y = []
    s = []
    for i in range(n):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    s = input()
    for i in range(n):
        if s[i] == "R":
            for j in range(n):
                if s[j] == "L":
                    if x[i] < x[j] and y[i] == y[j]:
                        print("Yes")
                        return
        else:
            for j in range(n):
                if s[j] == "R":
                    if x[i] > x[j] and y[i] == y[j]:
                        print("Yes")
                        return
    print("No")

if __name__ == '__main__':
    main()