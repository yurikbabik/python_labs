class Helicopter():
    def __init__(self, name="" , passengers=0 ,max_speed= 0 , production_year = 0  , manufacturer_country = ""):
        self.__name(name)
        self.__passengers(passengers)
        self.__max_speed(max_speed)
        self.production_year = production_year
        self.manufacturer_country = manufacturer_country

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_passengers(self):
        return self.__passengers
    def set_passengers(self, passengers):
        self.__passengers = passengers


    def get_max_speed(self):
        return self.__max_speed
    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def get_production_year(self):
        return self.production_year

    def get_manufacturer_country(self):
        return self.manufacturer_country

    def __str__(self):
        return f"name : {self.__name}, passengers : {self.__passengers}, max_speed : {self.__max_speed} км/год, production_year : {self.production_year},  manufacturer_country : {self.manufacturer_country}"

    def __repr__(self):
        return self.__str__()

    def __del__(self):
        print (f" Object {self.__name} is deleted")

def main ():
    heli1 = Helicopter("f16" ,250, 2400, 1976, "USA")
    heli2 = Helicopter("Apache", 4, 320, 1952, "USA")
    heli3 = Helicopter("Bell", 1, 1600, 1947, "USA")

    print(heli1)
    print(heli2)
    print(heli3)

if __name__ == "__main__":
    main()






