def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    if len(names) != len(set(names)):
        print('Yes')
    else:
        print('No')
