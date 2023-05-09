def main():
    H, W = map(int, input().split())
    count = 0
    for i in range(H):
        count += input().count('#')
    print(count)
