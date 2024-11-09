from datetime import datetime

#from this section is marlon's portion
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


#from this section is cat's portion

class Schedule:
    """Creates an object for a student's class schedule"""
    def __init__(self):
        """Initializes an empty list of events for the schedule."""
        self.events = []
        
    def remove_event(self, title):
        """Removes an event from the schedule based on the title.

         title: The title of the event to be removed.
        """
        self.events = [event for event in self.events if event.title != title]
        print(f"Event '{title}' removed from the schedule.")

    def add_event(self, event):
        """Adds an event to the schedule, checking for conflicts.

        :param event: An instance of the Event class.
        """
        if not self.has_conflict(event):
            self.events.append(event)
            print(f"Event '{event.title}' added toschedule.")
        else:
            print(f"Conflict detected: '{event.title}' overlaps with another event.")

    def has_conflict(self, new_event):
        """Checks if a new event conflicts with existing events.

        Args:
             new_event: An instance of the Event class to check.
        :return: True if there is a conflict, otherwise False.
        """
        for event in self.events:
            if (new_event.start_time < event.end_time and new_event.end_time > event.start_time):
                return True
        return False

    def upcoming_events(self, days=7):
        """Retrieves events occurring within the next specified number of days.

        Args
             days: The number of days to look ahead for upcoming events.
        return: A list of events happening within the specified time range.
        """
        now = datetime.now()
        future_date = now + timedelta(days=days)
        return [event for event in self.events if now <= event.start_time <= future_date]

    def __repr__(self):
        """String representation of the schedule showing all events."""
        if not self.events:
            return "The schedule is empty."
        return "\n".join([str(event) for event in sorted(self.events, key=lambda x: x.start_time)])
        
    #this is nick's portion:

    def add_recurring_event(self, event, recurrence, occurrences=10):
        """adds recurring events to our schedule. the events are based on how many times an event occurs

        :param event: an instance of the event class.
        :param recurrence: a string ('daily', 'weekly') indicating the recurrence pattern.
        :param occurrences: number of occurrences to add.
        """
        if recurrence not in ['daily', 'weekly']:
            print("unknown pattern. use 'daily' or 'weekly'.")
            return

        interval = timedelta(days=1) if recurrence == 'daily' else timedelta(weeks=1)
        for i in range(occurrences):
            new_event = Event(
                title=event.title,
                start_time=event.start_time + i * interval,
                end_time=event.end_time + i * interval,
                importance=event.importance,
                reccuring=recurrence
            )
            self.add_event(new_event)