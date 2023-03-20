class dealer(Account):
    def __init__(self, Dealer_Name, Office_hours, Area, Out_of_time, payment_info, insurerance, other, description, category, Review):
        self.__Dealer_Name = Dealer_Name
        self.__Office_hours = Office_hours
        self.__Area = Area
        self.__Out_of_time = Out_of_time
        self.__payment_info = payment_info
        self.__insurerance = insurerance
        self.__other = other
        self.__description = description
        self.__category = category
        self.__Review = Review

    def Create_car():
        pass

    def edit_car():
        pass

    def remove_car(self):
        pass

    def request_system():
        pass

    def update_account():
        pass

    def modify_dealer():
        pass

    def add_category():
        pass

class CarCategory:
    def __init__(self, car_with_driver, self_drive):
        self.__car_with_driver = [car_with_driver]
        self.__self_drive = [self_drive]

class Car:
    def __init__(self, Car_Name, Equipment, Price, Car_image, Year, Gear, Type, Large_bag, Small_bag, passenger, Car_status):
        self.__Car_Name= Car_Name
        self.__Equipment = Equipment
        self.__Price = Price
        self.__Car_image = Car_image
        self.__Year = Year
        self.__Gear = Gear
        self.__Type = Type
        self.__Large_bag = Large_bag 
        self.__Small_bag = Small_bag
        self.__passenger = passenger
        self.__Car_status = Car_status

    def check_car(self,car_status):
        pass
class Account:
    def __init__(self, username, name, surname, birthdate, email, tel):
        self._username = username
        self._name = name
        self._surname = surname
        self._birthdate = birthdate 
        self._email = email
        self._tel = tel  

    def check_info():
        pass

    def get_name(self):
        return self._name
    
    def get_username(self):
        return self._username
    
    def get_surname(self):
        return self._surname
    
    def get_profile_image(self):
        return self._profile_image
    
    def get_birth_date(self):
        return self._birthdate
    
class Booking():
    def __init__(self, First_Date, Last_Date, BookingStatus, price_added_on,Car_Name,amount):
        self.__First_Date = First_Date 
        self.__Last_Date = Last_Date
        self.__BookingStatus = BookingStatus
        self.__price_added_on = price_added_on
        self.__Car_Name = Car_Name
        self.__amount = amount
        

    def update_bookingstatus(self,First_date,Last_date):
        pass

class Region:
    def __init__(self, Region_TH, Province, Place):
        self.__Region_TH = [Region_TH]
        self.__Province = Province
        self.__Place = Place

    def search_car():
        pass

class BookCar:
    def __init__(self,First_day,Last_date):
        self.__First_date = First_day
        self.__last_date = Last_date

    def get_time(self):
        pass

class location:
    def __init__(self, get_car, return_car) -> None:
        self.__get_car = get_car
        self.__return_car = return_car

    def get_location(self):
        pass

class promotion:
    def __init__(self, promotion_list, special_price):
        self.__promotion_list = [promotion_list]
        self.__special_price = special_price

    def get_promotion(self):
        pass

class review:
    def __init__(self, rate, quality, service, accuracy, recommendation, comment):
        self.__rate = rate
        self.__quality = quality
        self.__service = service
        self.__accuracy = accuracy
        self.__recommendation = recommendation
        self.__comment = comment
    
