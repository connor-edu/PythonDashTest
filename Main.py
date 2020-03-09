from Invoice import Invoice

products = {}
total_amount = 0
repeat = ""
while True:
    product = input("What is your product: ")
    unitPrice = Invoice.inputNumber("Please enter unit price: ")
    qnt = Invoice.inputNumber("Please enter quantity of product: ")
    discount = Invoice.inputNumber("Discount percent (%): ")
    repeat = Invoice.inputAnswer("Another product? (y, n): ")
    result = Invoice.addProduct(qnt, unitPrice, discount)
    products[product] = result
    if (repeat == 'n'):
        break

total_amount = Invoice.totalPurePrice(products)

print('Your total pure price is: ', total_amount)
