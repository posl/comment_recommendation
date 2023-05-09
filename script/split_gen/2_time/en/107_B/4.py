def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    A = list(map(list, zip(*A)))
    A = [a for a in A if '#' in a]
    A = list(map(list, zip(*A)))
    for a in A:
        print(''.join(a))
main()
