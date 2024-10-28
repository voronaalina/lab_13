class CITY:
    def __init__(self, n, c, p):
        self.name = n
        self.country = c
        self.population = p
        print("City object has been created")

    def change_name(self, new_name):
        self.name = new_name

    def change_population(self, new_population):
        self.population = new_population
    
    def display(self):
        print("місто:",self.name, " країна:",self.country, " населення:",self.population)
    
    def delete(self):
        print(self.name, " видалено")

cities=[]
N = int(input("введіть кількість міст: "))
for i in range(N):
    name = input("введіть назву міста "+ str(i + 1) + ":")
    country = input("введіть країну для міста " + name + ":")
    population = int(input("введіть кількість населення для міста " + name + ":"))
    city = CITY(name, country, population)
    cities.append(city)

print("\nСписок міст:")
for city in cities:
    city.display()

city_to_del = input("\nвведіть місто для видалення: ")
cities = [city for city in cities if city.name != city_to_del]

print("\nоновлений список: ")
for city in cities:
    city.display()
    