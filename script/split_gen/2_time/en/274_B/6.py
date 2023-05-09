def main():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    for i in range(w):
        print(sum([1 for j in range(h) if a[j][i] == '#']))
