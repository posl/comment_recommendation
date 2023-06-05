def cal(n):
    res = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            res.append(i)
            if i != n//i:
                res.append(n//i)
    return sorted(res)
n = int(input())
res = cal(n)
for i in res:
    print(i)

if __name__ == '__main__':
    cal()