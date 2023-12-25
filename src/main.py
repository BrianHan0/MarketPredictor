

# api key : sk_61bac6eb481b4c05935309dabc73b65a

from src.data_processing.data_fetcher import get_stock_data,save_stock_data,clean_stock_data
from src.data_processing.data_loader import load_dataset,save_clean_data

def main():
    symbol = 'AAPL'
    api_key = 'sk_61bac6eb481b4c05935309dabc73b65a'
    data = get_stock_data(symbol,api_key)
    save_stock_data(data,symbol)




if __name__ == "__main__":
    main()
