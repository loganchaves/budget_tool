sav = []
spend = []

def punch():
        bills = input('Expected expense: ')
        net_pay = pay - bills 
        return net_pay
def savings():
    net_pay = punch()
    percent = input('%: ') 
    sav_total= float(net_pay * percent / 100)
    cash = net_pay - sav_total
    sav.append(sav_total)
    spend.append(cash) 
        
while True:
        pay = input('pay: ')
        savings()
        print('Savings')
        print(sav)
        print('Spend')
        print(spend)

    




