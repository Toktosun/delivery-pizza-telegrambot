from data import Pizza


def generate_pizzas():
    pizzas = [Pizza(name_pm='Маргарита', price_pm=300, size_pm=25, consist_pm='сыр, томаты'),
              Pizza(name_pm='Гавайская', price_pm=550, size_pm=35, consist_pm='сыр, ананас'),
              Pizza(name_pm='Пепперони', price_pm=495, size_pm=30, consist_pm='сыр, ветчина'),]
    return pizzas

