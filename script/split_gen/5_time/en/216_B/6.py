def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    print('Yes' if len(name) != len(set(map(tuple,name))) else 'No')
