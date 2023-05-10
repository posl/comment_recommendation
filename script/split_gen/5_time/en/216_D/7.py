def main():
    # Take input Here and Call solution function
    n, m = map(int, input().strip().split())
    a = []
    for i in range(m):
        a.append(list(map(int, input().strip().split())))
    print(solution(n, m, a))
