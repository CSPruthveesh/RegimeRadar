import asyncio
import json
import time
from datetime import datetime, timezone

# We'll import websockets. If not installed, we provide a graceful message.
try:
    import websockets
except ImportError:
    print("Warning: 'websockets' library is not installed in this environment.")
    print("Install it via: pip install websockets")
    websockets = None

async def binance_book_ticker_feed(symbol="bnbusdt"):
    if websockets is None:
        print("Cannot run live feed without 'websockets' library.")
        return
        
    url = f"wss://stream.binance.com:9443/ws/{symbol.lower()}@bookTicker"
    print(f"Connecting to live feed: {url}...")
    
    try:
        async with websockets.connect(url) as ws:
            print("Successfully connected to Binance Live Feed!")
            print(" ingesting ticks and calculating real-time features...\n")
            print(f"{'Timestamp (UTC)':<30} | {'BidPrice':<9} | {'AskPrice':<9} | {'Spread':<6} | {'Micro-Price':<11} | {'OBI L1':<6}")
            print("-" * 90)
            
            # Read first 15 messages for demonstration
            for _ in range(15):
                message = await ws.recv()
                data = json.loads(message)
                
                # Parse Binance bookTicker payload:
                # "b": best bid price, "B": best bid qty
                # "a": best ask price, "A": best ask qty
                bid_price = float(data.get("b", 0.0))
                bid_qty = float(data.get("B", 0.0))
                ask_price = float(data.get("a", 0.0))
                ask_qty = float(data.get("A", 0.0))
                
                # Real-time feature engineering
                spread = ask_price - bid_price
                micro_price = (bid_price * ask_qty + ask_price * bid_qty) / (bid_qty + ask_qty + 1e-9)
                obi_l1 = (bid_qty - ask_qty) / (bid_qty + ask_qty + 1e-9)
                
                utc_now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                
                print(f"{utc_now:<30} | {bid_price:<9.2f} | {ask_price:<9.2f} | {spread:<6.2f} | {micro_price:<11.4f} | {obi_l1:<+6.2f}")
                
            print("\nIngested 15 live ticks. Stream subscription closed successfully.")
            
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    # Run the client in the asyncio loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(binance_book_ticker_feed())
