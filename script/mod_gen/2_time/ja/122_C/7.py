def main():
    N, Q = map(int, input().split())
    S = input()
    LR = [list(map(int, input().split())) for _ in range(Q)]
    # ACを含む部分文字列の数を数える
    # 例：ACACTACG
    # AC: 1
    # ACA: 1
    # ACAC: 1
    # ACACT: 1
    # ACACTA: 1
    # ACACTAC: 2
    # ACACTACG: 2
    # つまり、ACの数を数える
    c = 0
    ac = []
    for s in S:
        if s == 'A':
            c += 1
        elif s == 'C' and c > 0:
            c -= 1
            ac.append(1)
        else:
            c = 0
    ac.append(0)
    ac.append(0)
    # 例：ACACTACG
    # AC: 1
    # ACA: 1
    # ACAC: 1
    # ACACT: 1
    # ACACTA: 1
    # ACACTAC: 2
    # ACACTACG: 2
    # つまり、ACの数を数える
    # ここで足し合わせていく
    # AC: 1
    # ACA: 1
    # ACAC: 1
    # ACACT: 2
    # ACACTA: 3
    # ACACTAC: 5
    # ACACTACG: 7
    for i in range(1, len(ac)):
        ac[i] += ac[i-1]
    # 例：ACACTACG
    # AC: 1
    # ACA: 1
    # ACAC: 1
    # ACACT: 2
    # ACACTA: 3
    # ACACTAC: 5
    # ACACTACG: 7
    # つまり、ACの数を数える
    # ここで足し合わせていく
    # AC: 1
    # ACA

if __name__ == '__main__':
    main()