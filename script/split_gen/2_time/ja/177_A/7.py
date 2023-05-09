def main():
    #標準入力から1行取得し、split()で分割し、map()でint型に変換し、リストに格納
    D,T,S = map(int, input().split())
    #待ち合わせ時刻までの距離を分速で割った値が待ち合わせ時刻以下であればYes
    if D/S <= T:
        print("Yes")
    else:
        print("No")
