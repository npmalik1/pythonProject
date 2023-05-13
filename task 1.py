dict1 = {
    'name': 'Diwakar',
    'salary': 50000.0,
    'id': 154,
    "city": "hyd",
    "profession": "developer",  # tester, admin, hr
    "city_type": "metropolitan",  # yes or no
    'address': {
        "street": "Main road",
        "pincode": 515511,
        "appartment": {

            "block": "C",
            "floor": "4rth"
        }
    }
}

prof = dict1['profession']
city_type = dict1['city_type']
salary = dict1['salary']  # 50000
if prof == "tester":
    if city_type == "metropolitan":
        # if dict1['id']>150:  # 144>150
            dict1["salary"] = salary+8000
        # else:
        #     dict1['salary'] = salary-10000
    else:
        dict1["salary"] = salary+4000
print(dict1)

