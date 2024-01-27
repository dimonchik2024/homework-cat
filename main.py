import random


class dog:
    def __init__(self, name="dog", job = None, home = None):
        self.name = name
        self.job = job
        self.home = home
        self.kitty = 100
        self.gladness = 50
        self.satiety = 50
    def get_home(self):
        pass
    def get_job(self):
        pass
    def eat(self):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
    def days_indexes(self, day):
        pass
    def is_alive(self):
        pass
    def live(self, day):
        pass

    class home:
        def __init__(self, brand_list):
            pass


brands_of_food_bags = {"Royal Canin": {"weight": 2, "age":1},
                 "Club 4 paws": {"weight": 14, "age": 1.3},
                 "Pedigree": {"weight": 8.4, "age":1},}
