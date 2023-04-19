



def main():
    pass

categories = {
    'horsepower': [
        {'name': 'slow_cars', 'min_hp': 0, 'max_hp': 120},
        {'name': 'fast_cars', 'min_hp': 120, 'max_hp': 180},
        {'name': 'sport_cars', 'min_hp': 180, 'max_hp': float('inf')},
    ],
    'price': [
        {'name': 'cheap_cars', 'min_price': 0, 'max_price': 1000},
        {'name': 'medium_cars', 'min_price': 1000, 'max_price': 5000},
        {'name': 'expensive_cars', 'min_price': 5000, 'max_price': float('inf')},
    ]
}



if __name__ == '__main__':
    main()
