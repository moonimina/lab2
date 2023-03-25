class Products:
    def __init__(self, prod_name, country, volume, summa):
        self.prod_name = prod_name
        self.country = country
        self.volume = volume
        self.summa = summa

    def __gt__(self, other):
        return self.prod_name > other.prod_name

    def __lt__(self, other):
       return self.prod_name < other.prod_name

    def __ge__(self, other):
        return self.prod_name >= other.prod_name

    def __le__(self, other):
       return self.prod_name <= other.prod_name

    def __eq__(self, other):
       return self.prod_name == other.prod_name