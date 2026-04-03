import os
from dotenv import load_dotenv
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel

from bot.client import BinanceClient
from bot.orders import execute_order
from bot.validators import validate_order
from bot.logging_config import setup_logging

load_dotenv()
setup_logging()


def get_order_input():
    print(Panel("📊 Enter Order Details", style="cyan"))

    symbol = Prompt.ask("Symbol").upper()
    side = Prompt.ask("Side", choices=["BUY", "SELL"])
    order_type = Prompt.ask(
        "Order Type",
        choices=["MARKET", "LIMIT", "STOP_LIMIT"]
    )
    quantity = Prompt.ask("Quantity")

    price = None
    stop_price = None

    if order_type == "LIMIT":
        price = Prompt.ask("Price")

    elif order_type == "STOP_LIMIT":
        stop_price = Prompt.ask("Stop Price")
        price = Prompt.ask("Limit Price")

    return {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "price": price,
        "stop_price": stop_price
    }


def confirm(order):
    print(Panel("🧾 Order Summary", style="yellow"))
    for k, v in order.items():
        if v:
            print(f"{k}: {v}")

    return Prompt.ask("Confirm?", choices=["y", "n"]) == "y"


def main():
    client = BinanceClient(
        os.getenv("API_KEY"),
        os.getenv("API_SECRET")
    )

    while True:
        print(Panel("🚀 Trading Bot", style="green"))
        print("1. Place Order")
        print("2. Exit")

        choice = Prompt.ask("Choose", choices=["1", "2"])

        if choice == "2":
            break

        try:
            order = get_order_input()

            validate_order(
                order["symbol"],
                order["side"],
                order["type"],
                order["quantity"],
                order.get("price"),
                order.get("stop_price")
            )

            if not confirm(order):
                print("❌ Cancelled")
                continue

            response = execute_order(client, order)

            print(Panel("✅ ORDER SUCCESS", style="green"))
            

        except Exception as e:
            print(f"[red]Error:[/red] {str(e)}")


if __name__ == "__main__":
    main()