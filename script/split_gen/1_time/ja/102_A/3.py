def main():
    N = int(input())
    # Nが2の倍数の場合
    if N % 2 == 0:
        print(N)
    # Nが2の倍数でない場合
    else:
        print(2*N)
