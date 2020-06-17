import math

indianMoney = [1,2,5,10,20,50,100,200,500,1000,2000]
def bill_count(totalMoney,billList):
    if(totalMoney<0):
        return "Inavalid Total Amount of Money"
    billList.sort()
    restMoney = totalMoney
    billCount = 0
    i = len(billList)-1
    while(restMoney >= 0 ):
        if(billList[i]>0 and billList[i] in indianMoney):
            temp = math.floor(restMoney/billList[i])
            billCount += temp
            restMoney -= temp*billList[i]
        elif billList[i] < 0:
            return "Invalid Bill Amount"
        elif not billList[i] in indianMoney:
            return "Bill amount should be in Indian standard system"
        i = i-1
    return billCount
    
print(bill_count(1001,[1,10,-20]))
