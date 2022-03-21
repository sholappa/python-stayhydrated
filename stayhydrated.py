import time 
from plyer import notification 

#Loop for notifications
while(True):
    notification.notify(
        #title here
        title = "Stay hydrated notifier",
        
        message = "Remember to drink water while working or gaming",
        #icon in .ico format
        app_icon = "bottle.ico",
    #stays for 25 seconds
        timeout  = 25
)

#notifies every 1 hour
    time.sleep(60*60*1)