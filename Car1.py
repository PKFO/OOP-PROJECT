
class Car:
    def __init__(self, car_name, car_image, car_plate,equipment, price, year, gear, cartype, largebag, smallbag, passenger, province, car_status):
        self.__carname = car_name
        self.__car_image = car_image
        self.__equipment = equipment
        self.__price = price
        self.__year = year
        self.__gear = gear
        self.__cartype = cartype
        self.__largebag = largebag
        self.__smallbag = smallbag
        self.__passenger = passenger
        self.__car_status = car_status
        self.__province = province
        self.__car_plate = car_plate
    
    @property
    def name(self):
        return self.__carname
    
    @property
    def car_plate(self):
        return self.__car_plate

    @property
    def province(self):
        return self.__province

    @property
    def carstatus(self):
        return self.__car_status

    @property
    def passenger(self):
        return self.__passenger

    @property
    def smallbag(self):
        return self.__smallbag

    @property
    def largebag(self):
        return self.__largebag
    
    @property
    def car_plate(self):
        return self.__car_plate
    
    @property
    def cargear(self):
        return self.__gear

    @property
    def caryear(self):
        return self.__year

    @property
    def carequipment(self):
        return self.__equipment

    @property
    def carimage(self):
        return self.__car_image
    
    @property
    def price(self):
        return self.__price
    
    @property
    def cartype(self):
        return self.__cartype
    
    def get_car_status(self):
        return self.__car_status

    def get_passenger(self):
        return self.__passenger
    
    def get_car_image(self):
        return self.__car_image
    
    def get_equipment(self):
        return self.__equipment
    
    def get_year(self):
        return self.__year
    
    def get_gear(self):
        return self.__gear
    
    def get_largebag(self):
        return self.__largebag
    
    def get_smallbag(self):
        return self.__smallbag
    
    def set_car_name(self,newcarname):
        self.__carname = newcarname 
        return self.__carname
     
    def set_car_equipment(self,newcarequipment):
        self.__equipment = newcarequipment
        return self.__equipment
    
    def set_car_price(self,newcareprice):
        self.__price = newcareprice
        return self.__price
    
    def set_car_year(self,newcaryear):
        self.__year = newcaryear
        return self.__year
    
    def set_car_gear(self,newcargear):
        self.__gear = newcargear
        return self.__gear
    
    def set_car_type(self,newcaretype):
        self.__cartype = newcaretype
        return self.__cartype
    
    def set_car_largebag(self,newcarlargebag):
        self.__largebag = newcarlargebag
        return self.__largebag
    
    def set_car_smallbag(self,newcarsmallbag):
        self.__smallbag = newcarsmallbag
        return self.__smallbag
    
    def set_car_passenger(self,newcarpassenger):
        self.__passenger = newcarpassenger
        return self.__passenger

    def get_price(self):
        return self.__price
    
    def get_cartype(self):
        return self.__cartype
    
    def get_passenger(self):
        return self.__passenger
    
    def get_car_image(self):
        return self.__car_image
    
    def get_equipment(self):
        return self.__equipment
    
    def get_year(self):
        return self.__year
    
    def get_gear(self):
        return self.__gear
    
    def get_largebag(self):
        return self.__largebag
    
    def get_smallbag(self):
        return self.__smallbag
    

    def __str__(self) :
        return str([{"Name" : self.__carname,"Image" : self.__car_image,"Equipment" : self.__equipment,"Price" : self.__price,"Year" : self.__year,"Gear" : self.__gear,"Cartype" : self.__cartype,"Largebag" : self.__largebag,"Smallbag" : self.__smallbag,"Passenger" : self.__passenger,"Carstatus" : self.__car_status}])

class Carcategory:

    def __init__(self):
        self.__carlist = []

    @property
    def carlist(self):
        return self.__carlist

    def add_to_carlist(self,car_name, car_image,car_plate, equipment, price, year, gear, cartype, largebag, smallbag, passenger,province):
        self.__carlist.append(Car(car_name, car_image,car_plate, equipment, price, year, gear, cartype, largebag, smallbag, passenger,province, True))
        return True
    
Carcatalog = Carcategory()
    