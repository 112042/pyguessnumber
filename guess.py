import random         #放入亂數函數

while True:           #強制迴圈(本程式希望手動離開，故下此強制回圈)
    
    numrange=input('請輸入要猜1~多少:\n')        #輸入一個值並給予numrange
    times=0                                    #判定次數
    

    if numrange.isdigit():                    #先判定輸入是否符合整數（isdigit()函數可以選擇輸入的字符串是否為純數；如果是純數，則返回True，否則返回False。）
        bignum=int(numrange)                  #針對輸入數字做資料型態轉換
        guesssmallnum=1                       #最小值為1
        guesssbignum=int(numrange)            #最大值為輸入的範圍值

        if bignum < 1:                        #如果輸入的值小於1，為不合法輸入
            print("請輸入大於1的數字謝謝\n")      
        elif bignum == 1:                     #如果輸入的值等於1，為不合法輸入
            print("你要猜什麼，請重新輸入\n")
        else:                                 #合法輸入下，開始設定參數
            rannum=random.randrange(1,bignum) #在合法輸入的範圍產生一個亂數   
            while True:                       #強制迴圈(本程式希望手動離開，故下此強制回圈)
                print("==========開始猜數字==========\n")
                guess=input('開始猜數字:\n')    #輸入一個值並給予guess
               
                
                if guess.isdigit():          #先判定輸入是否符合整數
                    guessnum=int(guess)      #針對輸入數字做資料型態轉換
                    
                    if guessnum < guesssmallnum:   #如果輸入的值小於猜數字範圍的最小值，為不合法輸入
                        times=times+1              #並增加一次次數
                        print("輸入值過小，從新輸入\n")
                    elif guessnum > guesssbignum:   #如果輸入的值大於猜數字範圍的最大值，為不合法輸入
                        times=times+1               #並增加一次次數
                        print("輸入值過大，從新輸入\n")
                    else:                          #如果輸入的值符合猜數字範圍的值，為合法輸入
                        if guessnum < rannum:      #輸入的值小於要猜數字的值
                            times=times+1          #增加一次次數
                            guesssmallnum=guessnum #將最小值互換
                            print("可惜沒猜中，下次的範圍為"+str(guesssmallnum)+"~"+str(guesssbignum))
                        elif  guessnum > rannum:  #輸入的值大於要猜數字的值
                            times=times+1         #增加一次次數
                            guesssbignum=guessnum #將最大值互換
                            print("可惜沒猜中，下次的範圍為"+str(guesssmallnum)+"~"+str(guesssbignum))
                        else:     #輸入的值等於要猜數字的值
                            times=times+1   #增加一次次數
                            print("恭喜猜中，數字為"+str(rannum)+"，你輸入數字為"+ str(guessnum)+'\n')
                            print("你總共猜了"+str(times)+"次(包含亂猜)"+'\n')
                            break   #離開猜數字流程(手動離開)
                else:   #輸入猜數字的值不符合整數
                    print("請輸入整數數字謝謝\n")
                    times=times+1    #增加一次次數
            
            print("==========是否離開===========\n")
            
            key=input("按q離開(其他任意鍵繼續)\n")   #輸入一個值並給予key
            if key=='q':                          #判定k是否符合其值
                print('離開遊戲\n')
                break                             #離開猜所有流程(手動離開)                        

    else:  #輸入範圍數字的值不符合整數
        print("請輸入整數數字謝謝\n")
