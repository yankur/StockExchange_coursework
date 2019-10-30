STOCK MARKET SIMULATOR

Application Stocks Market Simulator will allow all of its users to learn operating stocks on the market without loosing funds, thanks to the realistic simulation of all stock market processes.


РОБОТА ПРОГРАМИ

User gets charts with current stock prices of 30 companies. By evaluating stock market situation and his current(starting) capital, he can make a decision of buying or selling any company stocks. Program gets his requests and computes them, returning renewed chart of stock market situation after on cycle of sell-buy process. Then user can analyse his influence on global stock market. Simulation will last until program is runned.


MODULES DESCRIPTION

main.py - main module of the program 
graphs.py - visualisation of current data in graph 
market.py - contains class Market, which makes requests for current data, saves and calulates it   
network.py - contains class Network, class of AI and their interaction
user.py - class of the user, where his funds and desicions are saved
stocksim.kv - module Python kivi, GUI  


INSTALLING AND EXPERIENCING  

git clone https://github.com/yankur/StockExchange_coursework.git  
cd StockExchange_coursework/  
python main.py  
  
#with gui  
cd StockExchange_coursework/with_GUI  
python main_gui.py  
