### Scrapper script to scrape reviews from Google Play Store ###   
### and Apple Play Store                                     ### 



###  IMPORTS ###           
from play_scraper import search
import datetime
import csv
from pprint import pprint
from os import path
from app_store_scraper import AppStore
import subprocess



        
title_list=[]
##looP TO CONTROL OVER ALL ITERATION
while(True):

        ##Asking User for decsion between different store
        options=int(input("****MAIN MENU****\nPress 1 for Apple Store:\nPress 2 to exit:"))

         ##FOr apple store                
        if options==1:
            
            
            while(True):
                 ##search key to be entered in google play search box
                search_key=input("Enter the search query:")

                ##Search key to be pasted in the applestore_scraper.js file
                search="var search1= "+"'"+search_key+"'"

                ##opening both file and copiyng contents of applescraper in the applestorescraper file along with the search key
                with open ("applescraper.js","r+") as f:
                    #reading contents of the applescraper
                    content=f.readlines()
                    
                    with open("applestore_scraper.js" , "w") as f1:
                        #writing contents of and search key
                        f1.write(search)
                        f1.write("\n")
                        for each in content:
                            f1.write(each)
                ##A python module which allows us to run other programming language
                ##as a subprocess in this and output is in the form of strings
                sub = subprocess.check_output(['C:\\Program Files\\nodejs\\node.exe','applestore_scraper.js'],shell=True)
                
                ##decoding from bytes to character and spliting it to form list
                data=sub.decode().split("title:")
             
                ##Loop to store data in title_list
                for each in data:
                
                    if "url"  in each.split(",")[1]:
                    
                        title =  each.split(",")[0].strip("'")[2:]
                        title_list.append(title)
                y=1

                ##loop to show You the results
                for each in title_list:
                    print(str(y)+")"+each)
                    y=y+1

                ##decesion wether you are saatisfied with the searches or not    
                decesion4=int(input("Are these  searches related to you!!!? \nIf Yes press 1\nIf no press 2 to Enter related keywords:"))

                if decesion4==1:
                    ##selecting the app number
                    decesion4=int(input("Which NUmber of the app you want to see the reviews:"))


                    decesion5=input("Enter the code of the country:")
                    ##Now using APPstore module to get the reviews
                    try:
                        results = AppStore(country=decesion5, app_name=title_list[decesion4-1])
                    except:
                            print("**********************************************")
                            print("**********************************************")
                            print("Cannot receive this app data as its not on APP Store \nMight be deleted!!!")
                            print("********************ALERT**********************")
                            print("**********************************************")
                            break
                    try:     
                      
                            results = AppStore(country=decesion5, app_name=title_list[decesion4-1])
                    except :


                            print("**********************************************")
                            print("**********************************************")
                            print("Cpuntry code invalid\nEntering default code 'US'")
                            print("********************ALERT**********************")
                            print("***********************************************")
                            results = AppStore(country="us", app_name=title_list[decesion4-1]) 
                    
                    
                    
                    #decesion whether user want all or some
                    decesion3=int(input("IF you want 100 reviews press 1:\nIF you want all reviews press 2:"))
                    if decesion3==1:
                        ##if you want to see more reveiws just change how_many remeber how many alwasy counts 20 extra 
                        ##its better write 20 less
                        results_review =results.review(how_many=100)
                    if decesion3==2:
                        results_review =results.review()    
                    pprint( results.reviews)
                    print("**********************************************")
                    print("**********************************************")
                    print("**********************************************") 
                    ##decesion to see you aresatisfied
                    decesion=int(input("Are these  searches related to you!!!? \nIf Yes press 1\nIf no press 2 to Enter related keywords:"))    
                    if decesion==1:
                        ##checking if file exist not wrtitng titles to avoid redundancy 
                        if not path.exists(search_key+"Apple"+".csv"):
                         with open(search_key+"Apple"+".csv","a+",newline="") as f:
                            writer=csv.writer(f)
                            #gIVING TITLES
                            writer.writerow([ "APPNAME","TITLE","REVIEWER NAME","COMMENT","TIME","DATE","RATING"])

                        with open(search_key+"Apple"+".csv","a+",newline="",encoding='utf-8') as f:
                                        writer=csv.writer(f)
                                        ##retreiving data to be stored in csv file
                                        for key in results.reviews:

                                                ##i have used the try and except because Nonetyope exception is caused
                                                try:
                                                    date=key['date'].strftime("%m/%d/%Y")
                                                except :
                                                    date=None
                                                try:
                                                    time=key['date'].strftime("%H:%M:%S")
                                                except :
                                                    time=None
                                                
                                                ##wrtitng to the file
                                                writer.writerow([title_list[decesion4-1],key['title'], key['userName'], key['review'],time,date, key['rating']])

                        decesion=int(input("Press 1 to search more on Apple store: \nPress 2 to Exit:"))
                        if decesion==2:
                            break    
                title_list=[]            
    ##breaking of the final loop
        if options==2:
            break            