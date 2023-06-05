def problems235_a():
    abc = int(input())
    bca = abc//100*100 + abc%100//10*10 + abc%10
    cab = abc%10*100 + abc%100//10*10 + abc//100
    print(abc+bca+cab)
