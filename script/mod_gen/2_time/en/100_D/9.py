def main():
    N, M = map(int, input().split())
    # N: number of cakes
    # M: number of cakes to have
    # x_i, y_i, z_i (1 <= i <= N) are integers between -10^18 and 10^18 (inclusive)
    # x_i, y_i, z_i (1 <= i <= N) are the beauty, tastiness, popularity of the i-th kind of cake
    cakes = []
    for i in range(N):
        x, y, z = map(int, input().split())
        cakes.append((x, y, z))
    # The total beauty, tastiness and popularity will be as follows:
    # Beauty: sum of the beauty of the cakes
    # Tastiness: sum of the tastiness of the cakes
    # Popularity: sum of the popularity of the cakes
    # The value (the absolute value of the total beauty) + (the absolute value of the total tastiness) + (the absolute value of the total popularity) here is 13 + 17 + 26 = 56. This is the maximum value.
    # The value (the absolute value of the total beauty) + (the absolute value of the total tastiness) + (the absolute value of the total popularity) here is 21 + 24 + 9 = 54. This is the maximum value.
    # The value (the absolute value of the total beauty) + (the absolute value of the total tastiness) + (the absolute value of the total popularity) here is 323 + 66 + 249 = 638. This is the maximum value.
    # The value (the absolute value of the total beauty) + (the absolute value of the total tastiness) + (the absolute value of the total popularity) here is 30000000000. This is the maximum value.
    # The value (the absolute value of the total beauty) + (the absolute value of the total tastiness) + (the absolute value of the total popularity) here is 30000000000. This is the maximum value.
    # The value (the absolute value of the total beauty) + (the absolute value of the total tastiness) + (the absolute value of the total popularity) here is 30000000000. This is the maximum value.
    # The value (the absolute

if __name__ == '__main__':
    main()