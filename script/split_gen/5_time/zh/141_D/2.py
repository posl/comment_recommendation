def buyItemByDiscountTicket(itemPrice, ticketNum, ticketPrice):
    if ticketNum == 0:
        return itemPrice
    else:
        return buyItemByDiscountTicket(int(itemPrice/2), ticketNum-1, ticketPrice)
