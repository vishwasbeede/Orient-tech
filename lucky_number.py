def cal_lucky_num(x):
    y=x.split('-')
    z=y[2]+y[1]+y[0]
    decimal_num=str(bin(int(z)))[2:].count('1')
    return x,str(getSum(decimal_num))
    
# cal_lucky_num() 

def getSum(n):       
    strr = str(n) 
    list_number = list(map(int, strr.strip())) 
    return sum(list_number)
