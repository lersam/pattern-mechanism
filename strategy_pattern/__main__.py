from shopping_cart import ShoppingCart
from strategy import CreditCardPayment, PayPalPayment, CryptoPayment, DebitCardPayment

cart1 = ShoppingCart(CreditCardPayment())
cart1.checkout(100)

cart2 = ShoppingCart(PayPalPayment())
cart2.checkout(200)

cart3 = ShoppingCart(CryptoPayment())
cart3.checkout(300)

cart4 = ShoppingCart(DebitCardPayment())
cart4.checkout(400)
