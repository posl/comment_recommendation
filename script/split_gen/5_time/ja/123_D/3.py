def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ab = [i + j for i in a for j in b]
    ab.sort(reverse=True)
    abc = [i + j for i in ab[:k] for j in c]
    abc.sort(reverse=True)
    for i in range(k):
        print(abc[i])
