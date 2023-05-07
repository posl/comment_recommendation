def main():
    n = int(input())
    # 約数を求める
    div = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            div.append(i)
            if i**2 != n:
                div.append(n//i)
    div.sort()
    for i in div:
        print(i)
