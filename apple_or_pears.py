sell=0


def input_int(text):
    while True:
        try:
            return int(input(text))
        except:
            print("you need to pick a number.")




print("Hello Axel is selling apple for 7 dollars but Petra is selling pears for 13 dollars")

apple=input_int("so how many apple did Axel sell to day")

pear=input_int("but how many pears did Petra sell")
sell=1

print("let see who got more moneys")
pear*13
apple*7

if pear>apple:
    print(f"Petra has got more moneys")
elif apple>pear:
    print(f"Axel has  got more moneys")

elif apple==pear:
    print(f" they got the same amount of cash")















