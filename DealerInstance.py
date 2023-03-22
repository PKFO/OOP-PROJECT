import Class as C

dictdealer = {
    'Dealer1' : {
    'Dealer_Name' : 'Pon company',
    'profile_image': 'None',
    'Office_hours': '8.00-16.00',
    'Area' : 'BKK',
    'Out_of_time' : 'none',
    'insurerance' : '300,000 B',
    'payment_info' : 'Bank, credit card',
    'other' : 'none',
    'description' : 'none',
    'category' : [],
    'Review' : 'none',
    },
    'Dealer2' : {
    'Dealer_Name' : 'Focus company',
    'profile_image': 'None',
    'Office_hours': '8.00-17.00',
    'Area' : 'Buriram',
    'Out_of_time' : 'none',
    'insurerance' : '150,000 B',
    'payment_info' : 'Bank',
    'other' : 'none',
    'description' : 'I love cars!',
    'category' : [],
    'Review' : 'none',
    },
    'Dealer3' : {
    'Dealer_Name' : 'Guy company',
    'profile_image': 'None',
    'Office_hours': '7.00-13.00',
    'Area' : 'Chiang Mai',
    'Out_of_time' : 'tel',
    'insurerance' : '500,000 B',
    'payment_info' : 'Bank, credit card',
    'other' : 'none',
    'description' : 'believe in us!',
    'category' : [],
    'Review' : 'none',
    },

}

dealer1 = C.dealer(**dictdealer['Dealer1'])
dealer2 = C.dealer(**dictdealer['Dealer2'])
dealer3 = C.dealer(**dictdealer['Dealer3'])
