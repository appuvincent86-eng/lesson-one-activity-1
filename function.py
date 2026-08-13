#step1
name = input("what is your name? ")
def greet_customer(name):
    print(f"hello {name} and welcome to my lemonade stand!!!!!!!!!!!!!!!!!!!!!")
    print("we have the best lemonade in town")

#step2
greet_customer(name)

#step3
per_cup_sold=int(input("how many cups of lemonade do you want to buy? "))
if per_cup_sold > 3:
    print("thats alot") 
price_per_cup = float(input("how much is each cup of lemonade? "))

#step4
def calculate_total(per_cup_sold, price_per_cup):
    total=per_cup_sold*price_per_cup
    return total

#step5
total = calculate_total(per_cup_sold, price_per_cup)
print (total)
