def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())
    names = [x for x in zip(*names)]
    names = names[0] + names[1]
    if len(names) != len(set(names)):
        print('Yes')
    else:
        print('No')
