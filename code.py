def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    if city == "Tampa":
        return 220
    if city == "Pittsburgh":
        return 222
    if city == "Los Angeles":
        return 475
def rental_car_cost(days):
    rental=40*days
    if(days>=7):
        rental-=50
    elif days>=3:
        rental-=20
    return rental
def trip_cost(city,days,spending_money):
    sum = rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money
    print sum
