print("Welcome To Profit And Loss Program")
print("Designed and Programmed By Ayaan Ansari")
print("PROFIT AND LOSS PROGRAM")
print("Please enter your Cost Price:")
cp = int(input())
print("Please enter your selling price:")
sp = int(input())
if sp > cp :
    profit = int(sp) - int(cp)
    print("Congrats,You are in profit of:",profit)
else:
    loss = int(cp) - int(sp)
    print("Sorry,You are in loss of:",loss)
