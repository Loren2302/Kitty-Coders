"""Help students in major parts of their everyday lives """
from datetime import datetime
class Event:
    def __init__(self, title, start_time, end_time, importance=4, reccuring= None):
      """Hlps with event planning
      
      Attributes:
      Title: a string for the name of the event 
      Start_time= datetime object, that consists of date (month, year, day) and time (hour, minute)
      End_time= datatime object, similar to start_time
      importance= an integer, reprents how important an event can be, lower= more important, higher= less important. default is 4, but can change as needed 
      reccuring= a str, or None. It's a string like "daily" or "weekly." If None, it's a one-time event 
      """
      self.title= title 
      self.start_time= start_time
      self.end_time= end_time
      self.importance= importance
      self.reccuring= reccuring
      
    def __repr__(self):
        start_time_str = (f"{self.start_time.year}-{self.start_time.month}-{self.start_time.day} {self.start_time.hour}:{self.start_time.minute}")
        end_time_str= (f"{self.end_time.year}-{self.end_time.month}-{self.end_time.day} {self.end_time.hour}:{self.end_time.minute}")
        return (f"{self.title}: ({start_time_str} - {end_time_str})")
