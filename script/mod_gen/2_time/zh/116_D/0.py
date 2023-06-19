def solve(n, k, sushi):
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.append((0, 0))
    sushi.append((0, 0))
    # pr

if __name__ == '__main__':
    solve()