def main():
    N, X = map(int, input().split())
    L = map(int, input().split())
    D = [0]
    for i in L:
        D.append(D[-1] + i)
    print(sum([1 for i in D if i <= X]))
