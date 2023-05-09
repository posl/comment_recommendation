def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    d = [0]
    for i in range(N):
        d.append(d[i] + L[i])
    print(sum([1 for i in d if i <= X]))
