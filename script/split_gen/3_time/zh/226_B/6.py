def main():
    n = int(input())
    seq = []
    for i in range(n):
        seq.append(input().split())
    print(len(set(map(tuple,seq))))
