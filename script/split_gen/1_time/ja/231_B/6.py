def main():
    N = int(input())
    cands = []
    for i in range(N):
        cands.append(input())
    print(max(cands, key=cands.count))
