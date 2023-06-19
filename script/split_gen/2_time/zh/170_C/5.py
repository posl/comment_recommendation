def main():
    x,n = map(int, input().split())
    p = list(map(int, input().split()))
    p.append(x)
    p.sort()
    for i in range(101):
        if i not in p:
            break
    print(i)
