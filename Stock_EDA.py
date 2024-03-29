{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2021-08-26 17:11:11.064 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\quesa\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2021-08-26 17:11:11.295 NumExpr defaulting to 6 threads.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "import streamlit as st\n",
    "\n",
    "st.write(\"\"\"\n",
    "# Simple Stock Price App\n",
    "Shown are the stock **closing price** and ***volume*** of Google!\n",
    "\"\"\")\n",
    "\n",
    "# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75\n",
    "#define the ticker symbol\n",
    "tickerSymbol = 'GOOGL'\n",
    "#get data on this ticker\n",
    "tickerData = yf.Ticker(tickerSymbol)\n",
    "#get the historical prices for this ticker\n",
    "tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')\n",
    "# Open\tHigh\tLow\tClose\tVolume\tDividends\tStock Splits\n",
    "\n",
    "st.write(\"\"\"\n",
    "## Closing Price\n",
    "\"\"\")\n",
    "st.line_chart(tickerDf.Close)\n",
    "st.write(\"\"\"\n",
    "## Volume Price\n",
    "\"\"\")\n",
    "st.line_chart(tickerDf.Volume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
