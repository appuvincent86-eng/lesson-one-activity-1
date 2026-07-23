print("==============================================================")
print("   welcome to holiday planner!")
print("==============================================================")
print()

print("step 1 select your holiday")
print("12=mount everest")
print("11=grand canyon")
print()

choice=int(input("enter 11 or 12 : "))
print()

if choice==11:
    # Nested if -else - runs only when choice is 11
    print("step 2 select your activity")
    print("1=photographing")
    print("2=site seeing")
    print()

    grandcanyon_activity=int(input("enter 1 or 2 : "))
    print()

    if grandcanyon_activity==1:
        print("you have selected photographing at grand canyon")
        print("best time: morning")
        print("remember:camera")
    else:
        print("you have selected site seeing at grand canyon")
        print("best time: afternoon")
        print("remember:binoculars")
elif choice==12:
    print("choose your activity")
    print("1=climbing")
    print("2=camping")
    print()

    mounteverest_activity=int(input("enter 1 or 2 : "))

    if mounteverest_activity==1:
        print("you have selected climbing at mount everest")
        print("best time: morning")
        print("remember:climbing gear")
    else:
        print("you have selected camping at mount everest")
        print("best time: afternoon")
        print("remember:tent")
else:
    print("invalid choice")


    print()
    print("====================================================")
    print("   your holiday is planned! enjoy your trip!")
    print("====================================================")
