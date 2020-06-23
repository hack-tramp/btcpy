#!/usr/bin/python
# -*- coding: ascii -*-

import time , os, requests

#textart = ["0","1","2","3","4","5","6","7","8","9","."]
textart=[""" 
   ,a888a,    
 ,8P"' `"Y8,  
,8P       Y8, 
88         88 
88         88 
88         88 
88         88 
`8b       d8' 
 `8ba, ,ad8'  
   "Y888P"    """,
"""
    88        
  ,d88        
888888        
    88        
    88        
    88        
    88        
    88        
    88        
    88        """,
"""
 ad888888b,   
d8"     "88   
         88   
        d8P   
       a8P    
     ,d8P     
   ,d8P'      
 ,d8P'        
a88"          
88888888888   
""",
"""
 ad888888b,   
d8"     "88   
        a88   
       ,88P   
     aad8"    
     ""Y8,    
       `88b   
        "88   
Y8,     a88   
 "Y888888P'   
""",
"""
        a8    
      ,d88    
     a8P88    
   ,d8" 88    
  a8P'  88    
,d8"    88    
888888888888  
        88    
        88    
        88    
""",
"""
88888888888   
88            
88            
88  ____      
88a8PPPP8b,   
PP"     `8b   
         88   
         88   
Y8a     a8P   
 "Y88888P"    
""",
"""
  ad8888ba,   
 8P'    "Y8   
d8            
88            
88,dd888bb,   
88P'    `8b   
88       88   
88       88   
88a     a8P   
 "Y88888P"    
""",
"""
888888888888  
       ,88'   
     ,88"     
    ,88'      
 aaa888aa     
  ,8P         
 ,88          
 88'          
 88           
 88           
""",
"""
 ad88888ba    
d8"     "8b   
88       88   
Y8a     a8P   
 "Y8aaa8P"    
 ,d8"'"8b,    
d8"     "8b   
88       88   
Y8a     a8P   
 "Y88888P"    
""",
"""
 ad88888ba    
d8"     "88   
88       88   
88       88   
Y8,    ,d88   
 "PPPPPP"88   
         88   
         8P   
8b,    a8P    
`"Y8888P'     
""",
"""
              
              
              
              
              
              
              
 d8b          
 Y8P          
              
"""]

i = 0

class Price:
  def __init__(self, no, cstart, cend):
    self.no = no
    self.cstart = cstart
    self.cend = cend

price = []
colors = True
CRED = '\033[91m'
CGREEN = '\033[92m'
CEND_CODE = '\033[0m'
CEND = ''
CSTART = ''
pair = 'btcusd'
update_interval = 5
updint = str(update_interval)
cpair = pair[:3]+' to '+pair[-3:]
#max number of prices to be stored
maxprices = 100
#the last x number of those to be shown on top line
display_no = 10
list_info = 'Listing max '+str(display_no)+' latest prices out of '+str(maxprices)+' in memory\n'


while i<1:

    r = requests.get('https://api.cryptowat.ch/markets/coinbase-pro/'+pair+'/price')
    string_res = str(r.json()['result']['price'])
    string_btc = ['' for x in range(len(textart[0].splitlines()))]
    float_newprice = float(string_res)
    if len(price)>0:
      float_oldprice = float(price[len(price)-1].no)
    else:
      float_oldprice = 0.0
    os.system('cls')
    print('Showing currency pair '+cpair+' -- updated every '+updint+' seconds')
    t = time.time()

    print('Latest price at: '+time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(t)))
    print(list_info)
    for x in string_res:
      if x=='.':
         exploded = textart[int(10)].splitlines()
         for ln in range(len(exploded)):
            string_btc[ln] += exploded[ln]         
      else:
         exploded = textart[int(x)].splitlines()
         for ln in range(len(exploded)):
            string_btc[ln] += exploded[ln]
    
    if colors:
      if float_newprice > float_oldprice :
        CSTART = CGREEN; CEND = CEND_CODE
      elif float_newprice < float_oldprice :
        CSTART = CRED; CEND = CEND_CODE
      else:
        CSTART=''; CEND = ''
    
    if len(price)>maxprices:
      del price[0]
    price.append(Price(string_res,CSTART,CEND))
    
    lprice = len(price)
    disp_str = ''
    for p in range((lprice-1),-1,-1):
      if p>(lprice-display_no-1):
         disp_str = disp_str+ ' '+price[p].cstart+price[p].no+price[p].cend
            
    print(disp_str)
    
    for l in string_btc:
      print(CSTART+l+CEND)


    time.sleep(update_interval) 
