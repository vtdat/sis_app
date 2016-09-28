sisApp : core file
functions:
    + login(): to website
    + getmark(export = 0/1)
        - export = 0: don't export csv file
        - export = 1: do export csv file
    + getcpa(): calculate cpa
    + close(): close connection to website

how to use: 
    + create instance of sisApp: for example: app = sisApp()
    + login to website: app.login('username', 'password')
    + either call app.getcpa() or app.getmark(0/1)
    + close connection: app.close()
