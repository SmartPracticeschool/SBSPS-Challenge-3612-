import math
def bill_count(totalMoney,billList):
    if(totalMoney<0):
        return "Inavalid Total Amount of Money"
    billList.sort()
    restMoney = totalMoney
    billCount = 0
    i = len(billList)-1
    while(restMoney > 0):
        if(billList[i]>0):
            temp = math.floor(restMoney/billList[i])
            billCount += temp
            restMoney -= temp*billList[i]
         else:
            return "Invalid Bill Amount"
        i = i-1
    return billCount
    
