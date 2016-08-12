import simplegui

# define global variables
counter = 0
timer = 0
x = 0 # x is the number of successful stops
y = 0 # y is number of total stops

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
# A = the amount of minutes in that number
# B = the amount of tens of seconds
# C = the amount of seconds in excess of tens of seconds
# D = the amount of the remaining tenths of seconds

def test_of_reflexes():
    global x, y
    return 'Score ' + str (x) +'/'+ str(y)
    
def format(t):
    global counter
    A = counter // 600
    B = ((counter//100) % 6)
    C = (counter//10) % 10
    D = counter % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    timer.stop()
    global y
    global x
    y += 1
    if counter % 10 == 0:
        x += 1
        
def reset():
    global counter, x, y
    counter = 0
    x = 0
    y = 0
    
# define event handler for timer with 0.1 sec interval
def timer():
    global counter
    counter += 1
    return counter
    

# define draw handler
def current_time(canvas):
    canvas.draw_text(format(timer), (60, 110), 30, 'Red')
    canvas.draw_text(test_of_reflexes(), (110, 20), 20, 'White')
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 200, 200)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100, timer)

# register event handlers
frame.set_draw_handler(current_time)


# start frame
frame.start()
