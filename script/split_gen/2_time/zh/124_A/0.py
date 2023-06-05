def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ab = []
    for ai in a:
        for bi in b:
            ab.append(ai + bi)
    ab.sort(reverse=True)
    abc = []
    for i in range(min(k, len(ab))):
        for ci in c:
            abc.append(ab[i] + ci)
    abc.sort(reverse=True)
    for i in range(k):
        print(abc[i])
