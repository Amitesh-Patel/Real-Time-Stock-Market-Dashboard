import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts   -- #https://plotly.com/python/line-charts/
import matplotlib.pyplot as plt

from alpha_vantage.timeseries import TimeSeries
import time

api_key = "30N137BII0HWMIRB"

st.set_page_config(
    page_title = 'Real-Time Stock Market Dashboard',
    page_icon = '✅',
    layout = 'wide'
)
ts = TimeSeries(key = api_key,output_format = 'pandas')
symbol = st.text_input('Enter Stock Symbol (e.g., AAPL):')
if symbol:
    i = 1
    m=0
    while(i==1):
        st.write("This is",m,"th time")
        df,meta_data = ts.get_intraday(symbol = symbol,interval = "1min",outputsize = 'full')

        df.index.name = 'Date'
        df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        # df = pd.read_csv("data.csv")
        # [Date,Open,High,Low,Close,Volume]
        # dashboard title
        st.title("Real-Time / Live Data Science Dashboard")
        st.empty()
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.line(df, x=df.index, y=df["Close"])
            st.write(fig)

        stock_fig,stock_fig2 = st.columns(2)
        with stock_fig:
            st.title('Stock Price Over Time')
            st.markdown('This is a Streamlit app to display stock price over time.')

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(df.index, df['Close'], label='Close Price', color='blue')
            ax.set_xlabel('Date')
            ax.set_ylabel('Price')
            ax.set_title('Stock Price Over Time')
            ax.legend()
            ax.grid(True)

            # Display the Matplotlib plot in Streamlit
            st.pyplot(fig)

        # with stock_fig2:

        #     st.title('Volume Chart:')
        #     st.markdown('This is a Streamlit app to display Volume chart over date.')
        #     fig2, ax = plt.subplots(figsize=(10, 6))
        #     ax.bar(df["Date"], df['Volume'], label='Volume', color='green')
        #     ax.set_title('Trading Volume Over Time')
        #     ax.set_xlabel('Date')
        #     ax.set_ylabel('Volume')
        #     ax.legend()
        #     ax.grid(True)
        #     st.pyplot(fig2)

        figure1,figure2 = st.columns(2)
        with figure1 :
            st.title('Stock Price with Moving Averages')
            st.markdown('This is a Streamlit app to display Moving Averages')
            fig3,ax = plt.subplots(figsize=(10, 6))
            ax.plot(df.index, df['Close'], label='Close Price', color='blue')
            ax.plot(df.index, df['Close'].rolling(window=50).mean(), label='50-Day MA', color='orange')
            ax.plot(df.index, df['Close'].rolling(window=200).mean(), label='200-Day MA', color='red')
            ax.set_title('Stock Price with Moving Averages')
            ax.set_xlabel('Date')
            ax.set_ylabel('Price')
            ax.legend()
            ax.grid(True)
            st.pyplot(fig3)

        with figure2:
            st.title('Stock Price RSI')
            st.markdown('This is a Streamlit app to RSI')
            df['price_change'] = df['Close'].diff()
            lookback_period = 14

            # Calculate the average gain and average loss
            df['gain'] = df['price_change'].apply(lambda x: max(0, x))
            df['loss'] = df['price_change'].apply(lambda x: max(0, -x))
            df['avg_gain'] = df['gain'].rolling(window=lookback_period).mean()
            df['avg_loss'] = df['loss'].rolling(window=lookback_period).mean()

            # Calculate the relative strength (RS) and relative strength index (RSI)
            df['RS'] = df['avg_gain'] / df['avg_loss']
            df['RSI'] = 100 - (100 / (1 + df['RS']))
            df.drop(['price_change', 'gain', 'loss', 'avg_gain', 'avg_loss', 'RS'], axis=1, inplace=True)

            fig4,ax = plt.subplots(figsize=(10, 6))
            ax.plot(df.index, df['RSI'], label='RSI', color='purple')
            ax.axhline(70, color='red', linestyle='--', label='Overbought (70)')
            ax.axhline(30, color='green', linestyle='--', label='Oversold (30)')
            ax.set_title('Relative Strength Index (RSI) Over Time')
            ax.set_xlabel('Date')
            ax.set_ylabel('RSI')
            ax.legend()
            ax.grid(True)
            st.pyplot(fig4)

        st.write("Complete")
        m+=1
        time.sleep(60)










































#Put all this in a loop 
#So placeholder is the box we can assigned 3 boxes like this


#     with placeholder.container():
#         # create three columns
#         kpi1, kpi2, kpi3 = st.columns(3)

#         # fill in those three columns with respective metrics or KPIs 
#         kpi1.metric(label="Age ⏳", value=round(avg_age), delta= round(avg_age) - 10)
#         kpi2.metric(label="Married Count 💍", value= int(count_married), delta= - 10 + count_married)
#         kpi3.metric(label="A/C Balance ＄", value= f"$ {round(balance,2)} ", delta= - round(balance/count_married) * 100)



# #How to assigned two figures 
#     fig_col1, fig_col2 = st.columns(2)
#     with fig_col1:
#         st.markdown("### First Chart")
#         #write the code for plotting the data 
#         fig = px.density_heatmap(data_frame=df, y = 'age_new', x = 'marital')
#         st.write(fig)
        
#     with fig_col2:
#         st.markdown("### Second Chart")
#         fig2 = px.histogram(data_frame = df, x = 'age_new')
#         st.write(fig2)
#     st.markdown("### Detailed Data View")
#     st.dataframe(df)
#     time.sleep(1)

