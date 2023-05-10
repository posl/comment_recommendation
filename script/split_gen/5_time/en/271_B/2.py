def main():
    n, q = map(int, input().split())
    sequences = []
    for _ in range(n):
        sequences.append(list(map(int, input().split())))
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        print(sequences[query[0]-1][query[1]-1])
