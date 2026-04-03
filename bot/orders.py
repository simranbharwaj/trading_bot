import logging

logger = logging.getLogger(__name__)


def handle_market(client, symbol, side, quantity, **kwargs):
    params = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity
    }
    return client.place_order(params)


def handle_limit(client, symbol, side, quantity, price, **kwargs):
    params = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "timeInForce": "GTC"
    }
    return client.place_order(params)


def handle_stop_limit(client, symbol, side, quantity, price, stop_price, **kwargs):
    params = {
        "symbol": symbol,
        "side": side,
        "type": "STOP_LOSS_LIMIT",
        "quantity": quantity,
        "price": price,
        "stopPrice": stop_price,
        "timeInForce": "GTC"
    }
    return client.place_order(params)


ORDER_HANDLERS = {
    "MARKET": handle_market,
    "LIMIT": handle_limit,
    "STOP_LIMIT": handle_stop_limit,
}


def execute_order(client, order_data):
    order_type = order_data["type"]
    handler = ORDER_HANDLERS.get(order_type)

    if not handler:
        raise ValueError("Unsupported order type")

    logger.info(f"Executing {order_type}: {order_data}")

    response = handler(client, **order_data)

    logger.info(f"Response: {response}")

    return response