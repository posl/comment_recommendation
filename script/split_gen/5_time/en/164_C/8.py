def count_kinds_of_items():
    N = int(input())
    items = set()
    for i in range(N):
        items.add(input())
    print(len(items))
