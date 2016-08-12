# Mini-project description - "Stopwatch: The Game"

Our mini-project for this week will focus on combining text drawing in the canvas with timers to build a simple digital stopwatch that keeps track of the time in tenths of a second. The stopwatch should contain "Start", "Stop" and "Reset" buttons.

Mini-project development process

1. Construct a timer with an associated interval of 0.1 seconds whose event handler increments a global integer. (Remember that 𝚌𝚛𝚎𝚊𝚝𝚎_𝚝𝚒𝚖𝚎𝚛 takes the interval specified in milliseconds.) This integer will keep track of the time in tenths of seconds. Test your timer by printing this global integer to the console. Use the CodeSkulptor reset button in the blue menu bar to terminate your program and stop the timer and its print statements. Important: Do not use floating point numbers to keep track of tenths of a second! While it's certainly possible to get it working, the imprecision of floating point can make your life miserable. Use an integer instead, i.e., 12 represents 1.2 seconds.

2. Write the event handler function for the canvas that draws the current time (simply as an integer, you should not worry about formatting it yet) in the middle of the canvas. Remember that you will need to convert the current time into a string using 𝚜𝚝𝚛 before drawing it.

3. Add "Start" and "Stop" buttons whose event handlers start and stop the timer. Next, add a "Reset" button that stops the timer and reset the current time to zero. The stopwatch should be stopped when the frame opens.

4. Next, write a helper function 𝚏𝚘𝚛𝚖𝚊𝚝(𝚝) that returns a string of the form 𝙰:𝙱𝙲.𝙳 where 𝙰, 𝙲 and 𝙳 are digits in the range 0-9 and 𝙱 is in the range 0-5. 

5. Insert a call to the 𝚏𝚘𝚛𝚖𝚊𝚝 function into your draw handler to complete the stopwatch. (Note that the stopwatch need only work correctly up to 10 minutes, beyond that its behavior is your choice.)

6. Finally, to turn your stopwatch into a test of reflexes, add to two numerical counters that keep track of the number of times that you have stopped the watch and how many times you manage to stop the watch on a whole second (1.0, 2.0, 3.0, etc.). These counters should be drawn in the upper right-hand part of the stopwatch canvas in the form "𝚡/𝚢" where 𝚡 is the number of successful stops and 𝚢 is number of total stops. 

7. Add code to ensure that hitting the "Stop" button when the timer is already stopped does not change your score. We suggest that you add a global Boolean variable that is 𝚃𝚛𝚞𝚎 when the stopwatch is running and 𝙵𝚊𝚕𝚜𝚎 when the stopwatch is stopped. You can then use this value to determine whether to update the score when the "Stop" button is pressed.

8. Modify "Reset" so as to set these counters back to zero when clicked.
