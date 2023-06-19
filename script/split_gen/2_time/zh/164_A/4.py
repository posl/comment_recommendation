def main():
    sheep, wolf = map(int, input().split())
    if sheep > wolf:
        print("安全")
    else:
        print("不安全")
