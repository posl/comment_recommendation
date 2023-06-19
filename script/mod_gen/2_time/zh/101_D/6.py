def S(n):
    return sum(map(int, str(n)))
K = int(input())
ans = []
for i in range(1, 200):
    x = i * (10 ** (len(str(i)) - 1))
    while S(x) * (10 ** (len(str(x)) - 1)) < x:
        x += 1
    ans.append(x)
print(*ans[:K], sep='\n')

if __name__ == '__main__':
    S()