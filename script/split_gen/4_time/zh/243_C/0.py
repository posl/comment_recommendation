def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    s = input()
    #print(x)
    #print(y)
    #print(s)
    flag = False
    for i in range(n-1):
        if s[i] == 'R':
            for j in range(i+1,n):
                if s[j] == 'L':
                    if x[i] <= x[j] and y[i] == y[j]:
                        flag = True
                        break
        elif s[i] == 'L':
            for j in range(i+1,n):
                if s[j] == 'R':
                    if x[i] >= x[j] and y[i] == y[j]:
                        flag = True
                        break
    if flag:
        print("Yes")
    else:
        print("No")
