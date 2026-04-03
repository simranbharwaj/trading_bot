# 🚀 Trading Bot (Binance Testnet)

## 📌 Overview

This project is a Python-based trading bot that interacts with Binance Testnet APIs to place orders.
It features a clean modular architecture, interactive CLI, logging, and robust validation.

---

## ⚙️ Features

* Place MARKET, LIMIT, and STOP-LIMIT orders
* Supports BUY and SELL
* Interactive CLI (menu-driven)
* Input validation and error handling
* Structured logging (requests, responses, errors)
* Clean modular design (client, orders, validators)

---

## 📁 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── logs/
└── README.md
```

---

## 🔑 Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-link>
cd trading_bot
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Add API Keys

Create a `.env` file:

```
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## ▶️ How to Run

Run the CLI:

```
python cli.py
```

Follow the menu to place orders.

---

## 🧪 Example Orders

### MARKET Order

* Symbol: BTCUSDT
* Side: BUY
* Quantity: 0.001

### LIMIT Order

* Symbol: BTCUSDT
* Side: SELL
* Quantity: 0.001
* Price: 70000

---

## 📜 Logs

Logs are stored in:

```
logs/bot.log
```

Includes:

* API request
* API response
* Errors

---

## ⚠️ Assumptions

* Binance Spot Testnet is used due to regional restrictions
* Structure is compatible with Futures APIs with minor endpoint changes

---

## ✅ Output Example

```
ORDER PLACED SUCCESSFULLY
Order No: 12345678
Status: FILLED
```

---

## 💡 Future Improvements

* Add OCO / advanced order types
* Live price fetching
* Strategy-based automated trading
