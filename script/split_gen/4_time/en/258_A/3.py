def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print(f"{h+21:02}:{m:02}")
