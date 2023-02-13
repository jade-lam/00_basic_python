class Payment:
    payment_method = "card"

    def __init__(self,card_type):
        self.check_card_type(card_type)
        self.card_type = card_type

    def check_card_type(self, card_type):
        if card_type in ["Visa", "Master"]:
            print("Card Accepted")
        else:
            raise Exception("Card Rejected")

Payment("Visa")

#payment_with_visa = Payment("Visa")
#print(payment_with_visa.card_type)