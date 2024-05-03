import MetaTrader5 as mt5

def initialize_mt5():
    if not mt5.initialize():
        print("Failed to initialize MT5")
        mt5.shutdown()
    else:
        print("MT5 initialized successfully")

def get_account_info():
    account_info = mt5.account_info()
    if account_info is not None:
        print(account_info)
    else:
        print("Failed to get account info")

def main():
    initialize_mt5()
    get_account_info()
    # Qui puoi aggiungere ulteriori funzioni per il trading

if __name__ == "__main__":
    main()
