**Description**  
Trading robot.  
High-risk trading strategy.  
Trading with 10th leverage, or derivatives trading.   
Trading on any asset - stocks, currencies, cryptocurrencies, etc.  
Margin call when the asset price deviates by ~10%, based on the purchase price.
Close positions at the end of the day.

**trading.py**  
We create a random list of rates - changes in the asset price.  
We launch robots to buy and sell assets.  
We record all actions in the logs.txt file.  
We show a price chart, print a report and profit.  

**strategy.py**  
Example strategy.  
  
We buy one lot for 110 rubles, if the price goes up by 111 rubles. - we sell.  
Profit 1 rub., buy a lot for 111 rub.  
If the price goes down and reaches 108 rubles, we buy one more lot for 108 rubles,  
we get a portfolio consisting of two lots with an average price of 109 rubles.  
    Next - if the price returns to 110 rubles. - we sell purchased lots,  
    we get a profit of 2 rubles, buy 1 lot for 110 rubles.  
If the price goes down and reaches 105 rubles, we buy 2 more lots for 105 rubles,  
we get a portfolio consisting of four lots with an average price of 107 rubles.  
Next - if the price returns to 108 rubles. - we sell purchased lots,  
    we get a profit of 4 rubles, buy 1 lot for 108 rubles.  
If the price goes down and reaches 101 rubles, we buy 4 more lots for 101 rubles,  
we get a portfolio consisting of 8 lots with an average price of 104 rubles.  
    Next - if the price returns to 105 rubles. - we sell purchased lots,  
    we get a profit of 8 rubles, buy 1 lot for 105 rubles.  
If the price goes down and reaches ~96 rubles, we receive a Margin Call - the deposit is burned.  
  
<pre>
Price |  Add   |  Average  |Quantity|
      |        |  price    |        |
-------------------------------------
 110  |        |    110    |    1   |
 109  |        |           |        |
 108  |   +1   |    109    |    2   |
 107  |        |           |        |
 106  |        |           |        |
 105  |   +2   |    107    |    4   |
 104  |        |           |        |
 103  |        |           |        |
 102  |        |           |        |
 101  |   +4   |    105    |    8   |
 100  |        |           |        |
 99   |        |           |        |
 98   |        |           |        |
 97   |        |           |        |
 96   |        |           |    0   |
</pre>
    
At the same time, we launch a robot to sell this asset:  
We sell one lot for 110 rubles, if the price is down by 109 rubles. - we buy the sold lot.  
Profit 1 rub., we sell the lot for 109 rub.  
If the price goes up and reaches 112 rubles, we sell one lot for 112 rubles,  
we get a portfolio consisting of two lots with an average price of 111 rubles.  
    Next - if the price returns to 110 rubles. - we buy sold lots,  
    we get a profit of 2 rubles, we sell the lot for 110 rubles.  
If the price goes up and reaches 115 rubles, we sell 2 lots for 115 rubles,  
we get a portfolio consisting of four lots with an average price of 107 rubles.  
    Next - if the price returns to 112 rubles. - we buy sold lots,  
    we get a profit of 4 rubles, sell the lot for 112 rubles.  
If the price goes up and reaches 119 rubles, we sell 4 lots for 119 rubles,  
we get a portfolio consisting of 8 lots with an average price of 104 rubles.  
Next - if the price returns to 115 rubles. - we buy sold lots,  
    we get a profit of 8 rubles, sell the lot for 115 rubles.  
If the price goes up and reaches ~124 rubles, we receive a Margin Call - the deposit is burned.  
  
**write_logs.py**  
We record logs.  
All actions of buying, selling, taking profits are recorded in the logs.txt file.  
We record the time of the transaction, purchase or sale, profit taking or averaging, quantity.  
We write down a report, the final result after closing all positions.  
