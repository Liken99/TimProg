class Product:
    prod = []
    value = 0
    def __init__(self, prod, values):
        self.prod.append(prod)
        self.prod.append(values)

class Customer:
    product = ""
    gender = ""
    anger = 0
    money = 0
    customer_count = 0

    def __init__(self, products, genders, angers, moneys):
        self.product = products
        self.gender = genders
        self.anger = angers
        self.money = moneys
        Customer.customer_count += 1


class Seller:
    speed = 0
    sociability = 0
    seller_count = 0

    def __init__(self, speeds, sociabilitys):
        self.speed = speeds
        self.sociability = sociabilitys
        Seller.seller_count += 1


class Terminal():
    def purchase(self, money, value):
        if money < value:
            print("Недостаточно денег")
        elif money >= value:
            print("Покупка совершенна")


prod = Customer.customer_count + Customer.customer_count - 1
custom_1 = Customer("Хлеб", "М", 2, 50)
prod_1 = Product("Хлеб", 35)
pursh_1 = Terminal()
pursh_1.purchase(custom_1.money, prod_1.prod[prod])



custom_2 = Customer("Вода", "Ж", 4, 335)
prod_2 = Product("Вода", 65)
pursh_2 = Terminal()
pursh_2.purchase(custom_2.money, prod_2.prod[prod])



custom_3 = Customer("Чипсы", "М", 1, 110)
prod_3 = Product("Чипсы", 105)
pursh_3 = Terminal()
pursh_3.purchase(custom_3.money, prod_3.prod[prod])
