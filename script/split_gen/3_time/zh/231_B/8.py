def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input())
    print(max(name, key=name.count))
