"""
Demonstration of if statements.
"""
def greet(friend, money):
    """
    Greet people. Say hi if they are your friend and give
    them $20 if they are your friend and you have enough money.
    Steal $10 from them if they are not your friend.
    """
    
    if friend and (money > 20):
        print("Hi!")
        money = money - 20
    elif friend:
        print("\nHello.")
    else:
        print('HA HA!')
        money = money + 10
    return money



money = 15

money = greet(True, money)
print("\nMoney:", money)
print()



money = greet(False, money)
print("\nMoney:", money)
print()




money = greet(True, money)
print("\nMoney:", money)
print()




money = greet(False, money)
print("\nMoney:", money)
print()


money = greet(True, money)
print("\nMoney:", money)
print()