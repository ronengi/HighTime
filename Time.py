#!/usr/bin/python

#import copy


class Time:
    """Represents time of day

    Note:
        From the book: "Think Python", ch. 17

    Args:
        hour (int): (optional) the hours
        minute (int): (optional) the minutes
        second (int):(optional) the seconds

    Attributes:
        hour (int): how many hours || 0
        minute (int): how many minutes || 0
        second (int): how many seconds || 0
    
    TODO:
        * Fix / add all the remaining / missing docstrings

    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


    def __str__(self):
        """The str representation of the time in the format: hh:mm:ss"""
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)


    def __add__(self, other):
        """Adds another Time object or number of seconds

        Note:
            uses `assert` to verify the validity of the two added times

        Args:
            other (Time || int): what to add

        Returns:
            A new Time instance which is the result of the addition

        """
        assert valid_time(self) and valid_time(other)
        total_seconds = self.time_to_int()
        if isinstance(other, Time):
            total_seconds += other.time_to_int()
        else:
            total_seconds += other
        return int_to_time(total_seconds)


    def time_to_int(self):
        """convert h, m, s in decimal to number of seconds:
            a number in sexagecimal base"""
        m = self.hour * 60 + self.minute
        s = m * 60 + self.second
        return s


    """add seconds to time of self
    returns: new Time object
    """
    def increment(self, seconds):
        return int_to_time(self.time_to_int + seconds)


    """is self greater than the passed Time ?
    other: other Time to compare to self
    """
    def is_after(self, other):
        return (self.time_to_int() > other.time_to_int())


    def add_seconds(self, sec):
        self.second += sec
        self.minute += self.second // 60
        self.second = self.second % 60

        self.hour += self.minute // 60
        self.minute = self.minute % 60



def int_to_time(s):
    (minutes, seconds) = divmod(s, 60)
    (hours, minutes) = divmod(minutes, 60)
    t = Time(hours, minutes, seconds)
    return t



"""Check if a given value represents a truly valid time
attribute:  t    the value to check
returns:    True / False"""
def valid_time(t):
    if isinstance(t, int):      # allow integers to represent seconds
        return True
    elif isinstance(t, Time):
        if t.hour < 0 or t.minute < 0 or t.second < 0:
            return False
        elif t.hour >= 60 or t.minute >= 60 or t.second >= 60:
            return False
        else:
            return True
    else:
        return False


time = Time(9, 45)
print(time, end="")

print(time + Time(0, 16))

print(time + 17)



quit()

"""
time.hour = 11
time.minute = 59
time.second = 30

t2 = copy.deepcopy(time)
t2.hour = 12
t2.second = 12


time.print_time()
t2.print_time()
print(time.is_after(t2))

t3 = copy.deepcopy(t2)

add_seconds(t2, 8332)
t2.print_time()

t3 = int_to_time(t3.time_to_int() + 8332)
t3.print_time()

"""
