import Class as C

customer_info_dict = {
    "Renter1" : {
        "name" : "Harry Potter",
        "profile_image" : "",
        "birth_date" : "14/01/1944",
        "username" : "Hpotter",
        "password" : "iloveron"
    },
    "Renter2" : {
        "name" : "Lord Voldemort",
        "profile_image" : "",
        "birth_date" : "21/07/1456",
        "username" : "LordVoldemort",
        "password" : "iloveharry"
    },
    "Renter" : {
        "name" : "Ron Weasley",
        "profile_image" : "",
        "birth_date" : "09/11/1944",
        "username" : "RonWeasley",
        "password" : "iloveHermione"
    },
     "Renter4" : {
        "name" : "Hermione Granger",
        "profile_image" : "",
        "birth_date" : "31/07/1943",
        "username" : "HGranger",
        "password" : "perfectiseverything"
    },
    "Renter5" : {
        "name" : "Draco Malfoy",
        "profile_image" : "",
        "birth_date" : "23/11/1940",
        "username" : "Draco",
        "password" : "1212312121"
    },
    }

#Test 
customer_instance_list = []
for i in customer_info_dict:
    customer_instance_list.append(C.Account(**customer_info_dict[i]))