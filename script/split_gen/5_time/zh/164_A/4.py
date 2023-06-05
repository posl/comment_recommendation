def main():
    s,w = map(int, input().split())
    if s <= w:
        print("不安全")
    else:
        print("安全")
