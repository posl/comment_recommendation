def get_odds(n):
    odds = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            odds += 1
    return odds
