


from src.data_processing.data_fetcher import get_stock_data

def main():

    data = get_stock_data("AAPL")
    # data = get_clean_data(data)
    data.plot.line(y="Close", use_index=True)

    print(data)
if __name__ == "__main__":
    main()
