def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    print(max(l,key=l.count))
