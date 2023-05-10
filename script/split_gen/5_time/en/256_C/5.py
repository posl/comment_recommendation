def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    ans += (h1-1)*(w1-1)
    ans += (h1-1)*(w2-1)
    ans += (h1-1)*(w3-1)
    ans += (h2-1)*(w1-1)
    ans += (h2-1)*(w2-1)
    ans += (h2-1)*(w3-1)
    ans += (h3-1)*(w1-1)
    ans += (h3-1)*(w2-1)
    ans += (h3-1)*(w3-1)
    print(ans)
