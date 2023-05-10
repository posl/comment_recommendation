def main():
    N,X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print('Yes' if sum(a) <= X and X <= sum(b) else 'No')
