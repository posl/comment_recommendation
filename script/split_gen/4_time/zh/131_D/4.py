def main():
    N = int(input())
    works = []
    for _ in range(N):
        A, B = map(int, input().split())
        works.append((A, B))
    works.sort(key=lambda x: x[1])
    time = 0
    for A, B in works:
        if time + A > B:
            print('No')
            break
        time += A
    else:
        print('Yes')
