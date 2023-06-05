def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    print('Yes' if len(set(names)) < n else 'No')
