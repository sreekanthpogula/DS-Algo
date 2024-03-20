# volume of a sphere

def volume(r):
    return (4/3) * (3.14) * (r * r * r)

obj = volume(5)
print("Volume of the sphere with radius 5 is {0:.1f}".format(obj))


class Wholesale:
    @staticmethod
    def price_calculator(cover_price, shipping_charge, additional_copy_charge, n_of_copies):
        return (cover_price * 0.6) + shipping_charge + ((cover_price * 0.6 )+ additional_copy_charge) * (n_of_copies - 1)
    

obj1 = Wholesale.price_calculator(24.95, 3, 0.75, 60)
print("The wholesale price of the books is {0:.1f}$".format(obj1))


start_time = (6*60 + 52)*60
easy_pace_time = (8*60 + 15)*2
tempo_time = (7*60 + 12)*3

breakfast_hour = (start_time + easy_pace_time + tempo_time)/ (60 * 60)
breakfast_int_hour = int(breakfast_hour)

breakfast_min = (breakfast_hour - breakfast_int_hour)*60
breakfast_int_min = int(breakfast_min)

print("breakfast time is {}.{}".format(breakfast_int_hour, breakfast_int_min))


