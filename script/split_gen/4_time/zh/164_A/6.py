def main():
    sheep, wolf = map(int, input().split())
    if sheep <= wolf:
        print("不安全")
    else:
        print("安全")
