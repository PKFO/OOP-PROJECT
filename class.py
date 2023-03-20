class dealer:
    def __init__(self, Dealer_Name, Office_hours, Area, Out_of_time, payment_info, insurerance, other, description, category, Review):
        self._Dealer_Name = Dealer_Name
        self._Office_hours = Office_hours
        self._Area = Area
        self._Out_of_time = Out_of_time
        self._payment_info = payment_info
        self._insurerance = insurerance
        self._other = other
        self._description = description
        self._category = category
        self._Review = Review
    
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

class CarCategory:
    def __init__(self, car_with_driver, self_drive):
        self.car_with_driver = [car_with_driver]
        self.self_drive = [self_drive]

class Car:
    def __init__(self, Car_Name, Equipment, Price, Car_image, Year, Gear, Type, Large_bag, Small_bag, passenger, Car_status):
        self.Car_Name= Car_Name
        self.Equipment = Equipment
        self.Price = Price
        self.Car_image = Car_image
        self.Year = Year
        self.Gear = Gear
        self.Type = Type
        self.Large_bag = Large_bag 
        self.Small_bag = Small_bag
        self.passenger = passenger
        self.Car_status = Car_status

    def check_car(self,car_status):
        pass
        
class Account:
    def __init__(self, username, name, surname, birthdate, email, tel):
        self.username = username
        self.name = name
        self.surname = surname
        self.birthdate = birthdate 
        self.email = email
        self.tel = tel
    
    def check_info():
        pass

class Booking:
    def __init__(self, First_Date, Last_Date, BookingStatus, price_added_on):
        self.First_Date = First_Date 
        self.Last_Date = Last_Date
        self.BookingStatus = BookingStatus
        self.price_added_on = price_added_on

    def get_LocationTime(self):
        pass

    def update_bookingstatus(self,start_date,end_date):
        pass

class Region:
    def __init__(self, Region_TH, Province, Place):
        self.Region_TH = [Region_TH]
        self.Province = Province
        self.Place = Place

class location:
    def __init__(self, get_car, return_car) -> None:
        self.get_car = get_car
        self.return_car = return_car

    def search_car():
        pass

class promotion:
    def __init__(self, promotion_list, special_price):
        self.promotion_list = [promotion_list]
        self.special_price = special_price

class review:
    def __init__(self, rate, quality, service, accuracy, recommendation, comment):
        self.rate = rate
        self.quality = quality
        self.service = service
        self.accuracy = accuracy
        self.recommendation = recommendation
        self.comment = comment
  
