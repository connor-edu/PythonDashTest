class Invoice:

    @classmethod
    def addProduct(cls, qnt, price, discount):
        return {"qnt": qnt, "unit_price": price, "discount": discount}

    @classmethod
    def totalImpurePrice(cls, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v["unit_price"]) * int(v["qnt"])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    @classmethod
    def totalDiscountPrice(cls, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (float(v["unit_price"]) *
                               int(v["qnt"])) * float(v["discount"]) / 100
        total_discount = round(total_discount, 2)
        return total_discount

    @classmethod
    def totalPurePrice(cls, products):
        return cls.totalImpurePrice(products) - cls.totalDiscountPrice(products)

    @classmethod
    def inputAnswer(cls, inputValue):
        while True:
            userInput = input(inputValue)
            if (userInput in ["y", "n"]):
                return userInput
            print("y or n! Try again.")

    @classmethod
    def inputNumber(cls, inputValue):
        while True:
            try:
                userInput = float(input(inputValue))
                return userInput
            except ValueError:
                print("Not a number! Try again.")

    @classmethod
    def returnTotalQuantity(cls, products):
        num = 0
        for k, v in products.items():
            num += float(v["qnt"])
        return num

    @classmethod
    def calculateNumberOfItems(cls, products):
        num = len(products.items())
        return num