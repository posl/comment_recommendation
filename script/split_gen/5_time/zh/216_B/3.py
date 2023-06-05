def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    print('Yes' if len(names) != len(set(names)) else 'No')
