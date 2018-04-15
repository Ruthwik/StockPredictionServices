class StockPrice:
    def __init__(self, price):
        self.price = price

    def toJSON(self):
        return {'price': self.price}


class StockDate:
    def __init__(self, date):
        self.date = date

    def toJSON(self):
        return {"Stock": {'date': self.date}}