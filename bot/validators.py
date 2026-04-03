def validate_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Invalid order type")

    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError
    except:
        raise ValueError("Quantity must be positive")

    if order_type == "LIMIT":
        if not price:
            raise ValueError("LIMIT requires price")

    elif order_type == "STOP_LIMIT":
        if not price or not stop_price:
            raise ValueError("STOP_LIMIT requires price and stop price")

    return True