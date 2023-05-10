def solution():
    # This is the main function
    # Write your code here
    n, m = map(int, input().split())
    p_y = []
    for i in range(m):
        p, y = map(int, input().split())
        p_y.append((p, y, i))
    p_y.sort(key=lambda x: x[1])
    cities = [0] * (n + 1)
    for p, y, i in p_y:
        cities[p] += 1
        print(f"{p:06}{cities[p]:06}")
