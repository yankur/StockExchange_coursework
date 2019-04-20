class MarketADT:
    def __init__(self):
        self.companies = []
        self.basic = self.get_basic()
        self.active_offers = {company: [(None, 10000)] for company in self.companies}
        self.ais = []

    def get_basic(self):
        pass

    def add_ais(self, ais):
        pass

    def calculate(self):
        pass
