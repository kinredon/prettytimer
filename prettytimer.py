#!/usr/bin/env python
#
# Author: kinredon
# Email: kinredon@163.com
#

import time
import datetime
from collections import defaultdict
from prettytable import PrettyTable, MARKDOWN


class PrettyTimer():
    def __init__(self):
        """Returen a new PrettyTimer instance.

        Arguments: None

        """
        self._names = []
        self._start_timer = {}
        self._end_timer = {}
        self._time_gap = defaultdict(lambda: 0.0)

    def _is_duplicated(self, name):
        if name in self._names:
            raise f"The duplicated name: {name}"

    def start(self, name):
        """Start a timer named 'name' and record the start time of this timer.

        Arguments:

        name - string, an unique timer name
        """
        if name not in self._names:
            self._names.append(name)
        self._start_timer[name] = time.time()

    def end(self, name):
        """Record the end time of the 'name' timer and the timer lifespan.

        Arguments:

        name - string, an unique timer name
        """
        if name not in self._names:
            raise f"No such a timer: {name}"
        self._end_timer[name] = time.time()
        gap = self._end_timer[name] - self._start_timer[name]
        if gap < 0:
            raise f"Time gap is less than zero in timer {name}"
        self._time_gap[name] = gap

    def clloct(self):
        """Collect all the timer information, print it formatly.

        Arguments: None
        """
        pt = PrettyTable()
        pt.field_names = self._names
        pt.set_style(MARKDOWN)
        time_gap = []
        for name in self._names:
            time_gap.append(self._time_gap[name])
        pt.add_row(time_gap)
        pt.float_format = "0.3"
        print(pt)

    def eta(self, name, cur, total):
        """Calculate the Estimated Time of Arrival (ETA) for the specific timer 'name'.

        Arguments:

        name - string, an unique timer name
        cur - interger, current iterations of the running
        total - interger, total iterations of the running
        """
        gap = self._time_gap[name]
        eta = gap * (total - cur)
        eta = str(datetime.timedelta(seconds=eta))
        return eta

    def clear(self):
        self.__init__()


if __name__ == '__main__':
    timer = PrettyTimer()
    for i in range(100):
        timer.start("iter")
        time.sleep(2)
        timer.end("iter")
        eta = timer.eta("iter", i, 100)
        print(f"ETA: {eta}")
