def main():
    N,M = map(int, input().split())
    a = []
    for i in range(M):
        a.append(list(map(int, input().split())))
    print(len(a))
    return
