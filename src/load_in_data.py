import pandas as pd
import numpy as np





def load_data():

    def fill_zeros(string,length):
    
        while len(string)<length:
        
            string = "0"+string
    
        return string
 

    def func(x):
    
        x = str(x)
    
        return fill_zeros(x,6)





    b_price_df = pd.read_csv("data/price/b_stock_price.csv")
    a_price_df = pd.read_csv("data/price/a_stock_price.csv")
    ab_list = pd.read_csv("data/ticker_list/ab_list.csv")


    a_price_df["Stkcd"] = a_price_df.Stkcd.apply(func)
    b_price_df["Stkcd"] = b_price_df.Stkcd.apply(func)

    a_price_df["Trddt"] = pd.to_datetime(a_price_df.Trddt,format="%Y%m%d")
    b_price_df["Trddt"] = pd.to_datetime(b_price_df.Trddt,format="%Y%m%d")


    ab_list = ab_list.dropna()
    ab_list = ab_list.iloc[:,1:]


    ab_list["a_ticker"] = ab_list.a_ticker.astype(int)
    ab_list["a_ticker"] = ab_list.a_ticker.apply(func)
    ab_list["unique_id"] = range(0,len(ab_list))

    def func(x):
        x = str(x)
        x = "id_"+x
        return x
    ab_list["unique_id"] = ab_list.unique_id.apply(func)




    a_ticker_list = list(set(ab_list.a_ticker))
    b_ticker_list = list(set(ab_list.b_ticker))


    a_price_df["unique_id"] = "id"

    for a in a_ticker_list:
    
        unique_id = ab_list["unique_id"][ab_list.a_ticker==a].item()
    
        a_price_df["unique_id"][a_price_df.Stkcd == a] = unique_id


    b_price_df["unique_id"] = "id"

    for b in b_ticker_list:
    
        unique_id = ab_list["unique_id"][ab_list.b_ticker==b].item()
    
        b_price_df["unique_id"][b_price_df.Stkcd == str(b)] = unique_id

    return (a_price_df,b_price_df)





















