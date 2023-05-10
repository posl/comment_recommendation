def count_kinds_of_items():
    N = int(input())
    items = set()
    for i in range(N):
        items.add(input())
    print(len(items))

if __name__ == '__main__':
    count_kinds_of_items()