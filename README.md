# PrettyTimer

PrettyTimer is a sssuper simple yet useful tool for you to collct the running time of the codeblock.

If you want to evaluate the running time of your codeblock, for example, in a machine learning project, the program has serveral stages: data load, model forward, gradient backward, etc. Even you will statistic running time more than ten codeblocks. The general way is to implement it like this:
```python

import time

start_time_load_data = time.time()
time.sleep(3)
end_time_load_data = time.time()
print(end_time_load_data - start_time_load_data)

start_time_forward = time.time()
time.sleep(3)
end_time_forward = time.time()
print(end_time_forward - start_time_forward)

start_time_backward = time.time()
time.sleep(3)
end_time_backward = time.time()
print(end_time_backward - start_time_backward)

start_time_clloct = time.time()
time.sleep(3)
end_time_clloct = time.time()
print(end_time_clloct - start_time_clloct)


```

PrettyTimer will reproduce it effiently and elegantly as follows:
```python'
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
```

The cllocted information is a Markdown table style which can be copied and pasetd to your Markdown document.

![./clloct_table.png](https://github.com/kinredon/prettytimer/blob/master/clloct_table.png)

Moreover, Prettytimer provide a ETA (Estimated Time of Arrival) method:
```python
timer.eta(NAME, ITER, TOTAL)
```
where NANE is an unique identifier to a timer, ITER is current iteration and TOTAL is total iterations of your training schedule.

That's all! Pretty concise, right? 

Maybe there is a more graceful way to implement this, if yes, please tell me.

# Installation
Install via pip:

    pip install -U prettytimer
    
Install latest development version:

    pip install -U git+git@github.com:kinredon/prettytimer.git

