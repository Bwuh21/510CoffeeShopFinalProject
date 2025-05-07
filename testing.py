automaton = {
    'start': {
        'Latte': 'got_order_type',
        'Espresso': 'got_order_type',
        'Cappuccino': 'got_order_type',
        'ColdBrew': 'got_order_type',
        'Chai': 'got_order_type',
        'Matcha': 'got_order_type',
    },
    'got_order_type': {
        'Small': 'got_size',
        'Medium': 'got_size',
        'Large': 'got_size',
    },
    'got_size': {
        'Hot': 'got_temp',
        'Iced': 'got_temp',
    },
    'got_temp': {
        'Whole': 'got_milk', 'Oat': 'got_milk', 'Skim': 'got_milk', 'Almond': 'got_milk', 'Checkout': 'end'
    },
    'got_milk': {
        'Vanilla': 'got_flavor', 'Caramel': 'got_flavor', 'Mocha': 'got_flavor', 'Hazelnut': 'got_flavor', 'CookieButter': 'got_flavor', 'Honey': 'got_flavor', 'SfVanilla': 'got_flavor', 'Raspberry': 'got_flavor', 'Blueberry': 'got_flavor', 'Checkout': 'end'
    },
    'got_flavor': {
        'Whip': 'got_topping', 'Coldfoam': 'got_topping', 'Cinnamon': 'got_topping', 'Salt': 'got_topping', 'CookieButterChunks': 'got_topping', 'BlueberryChunks': 'got_topping', 'Checkout': 'end'
    },
    'got_topping': {
        'ExtraShot': 'got_addon', 'LightIce': 'got_addon', 'Decaf': 'got_addon', 'Stevia': 'got_addon', 'ExtraMatcha': 'got_addon', 'ExtraSweetener': 'got_addon', 'Checkout': 'end'
    },
    'got_addon': {
        'Name': 'got_name', 'Checkout': 'end'
    },
    'got_name': {
        'ForHere': 'got_pickup', 'ToGo': 'got_pickup', 'Checkout': 'end'
    },
    'got_pickup': {
        'Checkout': 'end'
    }
}

def accept(automaton, input_string):
    w = input_string.split()
    state = 'start'
    for symbol in w:
        if symbol in automaton.get(state, {}):
            state = automaton[state][symbol]
        elif state == 'got_name':
            state = 'got_pickup'  # Allow any name
        elif state == 'got_addon' and symbol.startswith("Name"):
            state = 'got_name'  # Allow custom names
        else:
            return "Reject"
    return "Accept" if state == 'end' else "Reject"

# Example usage
user_input = input("Enter your order: ")
print(accept(automaton, user_input))
