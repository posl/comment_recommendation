def isok(baggage,box):
    baggage.sort(key=lambda x:x[1],reverse=True)
    box.sort(reverse=True)
    for i in box:
        for j in range(len(baggage)):
            if i>=baggage[j][0]:
                box.remove(i)
                baggage.remove(baggage[j])
                break
    if len(baggage)==0:
        return True
    else:
        return False

if __name__ == '__main__':
    isok()