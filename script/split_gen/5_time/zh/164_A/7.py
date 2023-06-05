def main():
    S, W = map(int, input().split())
    if S > W:
        print('安全')
    else:
        print('不安全')
