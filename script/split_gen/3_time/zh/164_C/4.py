def main():
    n = int(input())
    items = []
    for i in range(n):
        items.append(input())
    print(len(set(items)))
