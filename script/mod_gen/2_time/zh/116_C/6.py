def water_the_flowers(N, H):
    ans = 0
    for i in range(N):
        ans += H[i]
    return ans

if __name__ == '__main__':
    water_the_flowers()