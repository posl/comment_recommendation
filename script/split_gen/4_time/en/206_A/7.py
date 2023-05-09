def main():
    N = int(input())
    print("Yay!" if N*108//100 < 206 else ":(" if N*108//100 > 206 else "so-so")
