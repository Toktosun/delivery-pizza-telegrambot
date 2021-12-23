class Product:
    def __init__(self, name_pm, price_pm):
        self.name = name_pm
        self.price = price_pm

    def get_name_with_price(self):
        return f'{self.name} - {self.price} сом'


class Pizza(Product):
    def __init__(self, name_pm, price_pm, size_pm, consist_pm):
        super().__init__(name_pm, price_pm)
        self.size = size_pm
        self.consist = consist_pm


class Drink(Product):
    def __init__(self, name_pm, price_pm, volume_pm, is_gas_pm):
        super().__init__(name_pm, price_pm)
        self.volume = volume_pm  # объем
        self.is_gas = is_gas_pm

    def __str__(self):  # когда мы принтует данный объект
        return f'Наш напиток: {self.name}'

    def __len__(self):
        return 777
