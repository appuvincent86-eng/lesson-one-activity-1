print("==============================================================")
print("    welcome to game builder:)")
print("==============================================================")
print()

print("select game or food" )
print("game=18" )
print("food=711" )
print()
choice=int(input("enter 18 or 711 "))
if choice==18:
    print("you have selected game")
    print("what is your favourite game choose one")
    print("crossout=11")
    print("roblox=12")
    choice=int(input("enter 11 or 12 "))
    if choice==11:
        print("you have selected crossout")
    elif choice==12:
        print("you have selected roblox")
    else:
         print("invalid choice")