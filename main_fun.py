class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.money = money
        self.coffee_menu = {
            "espresso": {"cost": 1.5, "water": 50, "milk": 0, "coffee_beans": 18},
            "latte": {"cost": 2.5, "water": 200, "milk": 150, "coffee_beans": 24},
            "cappuccino": {"cost": 3.0, "water": 250, "milk": 100, "coffee_beans": 24},
            "mocha": {"cost": 3.5, "water": 200, "milk": 100, "coffee_beans": 20},
            "americano": {"cost": 2.0, "water": 150, "milk": 0, "coffee_beans": 15},
        }
    
    def get_report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee Beans: {self.coffee_beans}g")
        print(f"Money: ${self.money:.2f}")

    def turn_off(self):
        print("Turning off the coffee machine. Goodbye!")
        exit()

    def check_resources(self, water_needed, milk_needed, beans_needed):
        if self.water < water_needed:
            print("Sorry, not enough water!")
            return False
        if self.milk < milk_needed:
            print("Sorry, not enough milk!")
            return False
        if self.coffee_beans < beans_needed:
            print("Sorry, not enough coffee beans!")
            return False
        return True

    def make_coffee(self, coffee_type):
        coffee = self.coffee_menu[coffee_type]
        if self.check_resources(coffee['water'], coffee['milk'], coffee['coffee_beans']):
            total_money = self.insert_coins()
            if self.check_transaction(coffee['cost'], total_money):
                self.serve_coffee(coffee_type)
                self.give_change(coffee['cost'], total_money)
        else:
            print(f"Cannot make {coffee_type}, not enough resources.")

    def insert_coins(self):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        total_money = quarters + dimes + nickels + pennies
        return total_money

    def check_transaction(self, cost, total_money):
        if total_money >= cost:
            self.money += cost
            return True
        else:
            print("Sorry, not enough money. Money refunded.")
            return False

    def give_change(self, cost, total_money):
        change = total_money - cost
        if change > 0:
            print(f"Here is your change: ${change:.2f}")

    def serve_coffee(self, coffee_type):
        coffee = self.coffee_menu[coffee_type]
        self.water -= coffee['water']
        self.milk -= coffee['milk']
        self.coffee_beans -= coffee['coffee_beans']
        print(f"Here is your {coffee_type}. Enjoy!")

    def check_resource_alert(self):
        if self.water < 200:
            print("Warning: Low water!")
        if self.milk < 150:
            print("Warning: Low milk!")
        if self.coffee_beans < 24:
            print("Warning: Low coffee beans!")


def main():
    coffee_machine = CoffeeMachine(water=1000, milk=500, coffee_beans=200, money=0)

    while True:
        coffee_machine.check_resource_alert()
        choice = input("What would you like? (espresso/latte/cappuccino/mocha/americano/off/report): ").lower()
        if choice == "off":
            coffee_machine.turn_off()
        elif choice == "report":
            coffee_machine.get_report()
        elif choice in coffee_machine.coffee_menu:
            coffee_machine.make_coffee(choice)
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
