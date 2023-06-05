def get_ranking(n, m, a):
    ranking = [i for i in range(1, 2 * n + 1)]
    for i in range(m):
        ranking = get_ranking_once(n, ranking, a[i])
    return ranking
