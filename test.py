import time
from prettytimer import PrettyTimer

timer = PrettyTimer()

timer.start('load_data')
time.sleep(3)
timer.end('load_data')

timer.start('forward')
time.sleep(3)
timer.end('forward')

timer.start('backward')
time.sleep(3)
timer.end('backward')

timer.start('clloct')
time.sleep(3)
timer.end('clloct')

timer.clloct()
