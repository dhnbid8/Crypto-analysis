import ast
import os
from colorama import Fore

os.system('clear')

def to_organize(file_name):
    file = open("data/" + file_name)
    data = file.read()
    data = ast.literal_eval(data)
    return data

file_name = input("enter first")
data = to_organize(file_name)
file_name = "2021-11-22-03:31:43.txt"
data2 = to_organize(file_name)

for i in range(4999):
        coin_name = data['data'][i]['symbol']
        coin_name2 = data2['data'][i]['symbol']
        if coin_name == coin_name2:
            f_price = data['data'][i]['quote']['USD']['price']
            s_price = data2['data'][i]['quote']['USD']['price']
            print("\n"+ str(i) +" -----------------------------")
            print(f_price)
            print(s_price)
            dis2 = f_price - s_price
            dis2 = round((dis2)/3 , 4)
            if f_price > s_price :
                Dispute = (s_price - f_price) / abs(f_price) * 100
                
                print(dis2)
                print(Fore.RED + coin_name + " : " +str(Dispute)+"%" + Fore.WHITE) 
            else:
                Dispute = (s_price - f_price) / abs(f_price) * 100
                
                print(dis2)
                print(Fore.GREEN+coin_name+ " : " +str(Dispute)+"%"+Fore.WHITE)
        else:
            continue