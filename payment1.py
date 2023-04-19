from Account import *
class Payment(Booked):
    def __init__(self,car,amount):
        super().__init__(car.price)
        self.__amount = amount
        
    def process_payment(self,coupon_code):
        self.amount = Coupon.use_coupon(coupon_code)
        print(f"Payment of {self.amount} processed.")


class PaymentByBank(Payment):
    def __init__(self, amount,payment_code,referral_code):
        super().__init__(amount)    
        self.__paynemt_code = payment_code
        self.__referral_code = referral_code

    def process_payment(self):
        return (f"Payment by bank of {self.amount} processed.")

class CreditCardPayment(Payment):

    def __init__(self, amount, card_number, expiry_date, cvv):
        super().__init__(amount)
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
    
    def process_payment(self):
        # code to process credit card payment here
        print(f"Credit card payment of {self.amount} processed.")

class CashPayment(Payment):
    def __init__(self, amount, currency):
        super().__init__(amount)
        self.currency = currency
    
    def process_payment(self):
        # code to process cash payment here
        print(f"Cash payment of {self.amount} {self.currency} processed.")