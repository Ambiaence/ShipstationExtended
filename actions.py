from order import Order

def default_action(order):
    if type(item) != type(Order):
        message = "product must be of type Product. Current type is "
        message = message + str(type(product))
        raise Exception(message)
