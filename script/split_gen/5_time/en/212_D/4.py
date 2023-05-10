def main():
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    bag = []
    smallest = 0
    for query in queries:
        if query[0] == 1:
            bag.append(query[1])
        elif query[0] == 2:
            bag = [i+query[1] for i in bag]
        elif query[0] == 3:
            smallest = min(bag)
            bag.remove(smallest)
            print(smallest)
