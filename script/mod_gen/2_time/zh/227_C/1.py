def get_area(a, b):
    return 4*a*b + 3*a + 3*b
N = int(input())
S = list(map(int, input().split()))
count = 0
for i in range(N):
    for j in range(i+1, N):
        if S[i] == S[j]:
            continue
        for a in range(1, 1000):
            for b in range(1, 1000):
                if S[i] == get_area(a, b) and S[j] == get_area(a, b):
                    count += 1
print(count)

if __name__ == '__main__':
    get_area()