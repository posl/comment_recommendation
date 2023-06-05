def func1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        flag = True
        for j in range(n):
            if i != j and a[j] % a[i] == 0:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    func1()