from datetime import datetime
class Schedule:
    "Creates an object for a student's class schedule
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



        
