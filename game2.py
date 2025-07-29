import random
from time import sleep
print("          <let's play game>")
print("if you want exit from game type 'exit/bye'")
dic={"gun":"snake","water":"gun","snake":"water"}
ls=list(dic.keys())
print('\nchoose one',ls)
def process():
    i=0
    while i<5:
        for a in range(0,3):
            print("\rcomp choose :",ls[a],end="")
            sleep(.1)
        i += 1
while True:
    user=input("\ntype : ").lower()
    if user == "exit" or user == "bye":
        exit()
    elif user not in ls:
        print("wrong input")
        continue
    comp=random.choice(ls)
    process()
    print(f"\rcomp choose : {comp}  ",end="")
    if comp == user:
        print("\nmatch draw")
    elif comp == dic.get(user):
        print("\nyou win")
    else:
        print("\nyou lose")
