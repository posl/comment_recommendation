def main():
    n = int(input())
    result = set()
    for i in range(n):
        line = input().split()
        result.add(tuple(line[1:]))
    print(len(result))
