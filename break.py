import time
import webbrowser

counter = 0
print("This program started on " + time.ctime())
while counter < 3:
    time.sleep(3)
    webbrowser.open("http://www.youtube.com/")
    counter +=1
