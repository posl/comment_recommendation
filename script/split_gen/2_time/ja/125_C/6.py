def main():
    N = int(input())
    A = list(map(int, input().split()))
    # Aの最大値を求める
    max_A = max(A)
    # Aの最大値の約数を求める
    max_A_divs = []
    for i in range(1, int(max_A**0.5)+1):
        if max_A % i == 0:
            max_A_divs.append(i)
            if i != max_A // i:
                max_A_divs.append(max_A // i)
    # Aの最大値の約数のうち、Aの約数になっているものを求める
    A_divs = []
    for div in max_A_divs:
        for a in A:
            if a % div != 0:
                break
        else:
            A_divs.append(div)
    # Aの最大値の約数のうち、Aの約数になっているもののうち、最大のものを求める
    print(max(A_divs))
