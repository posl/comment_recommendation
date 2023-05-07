def main():
    X, Y, A, B = map(int, input().split())
    # カコモンジムの回数
    count = 0
    # カコモンジムの回数を1増やす
    while X * A < Y and X * A < X + B:
        X = X * A
        count += 1
    # AtCoderジムの回数
    count += (Y - X - 1) // B
    print(count)
