#Task 2: Event Management System Enhancement
# - Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. 
# Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
    def add_participant(self):
        self.participant_count += 1
    
    def display_count(self):
        print(f"Event name '{self.name}' on {self.date} has {self.participant_count} participants")

participants = {}

def add_count(name, date):
    event_pair = (name, date)
    if event_pair in participants: # for existing events
        participants[event_pair].add_participant()
        print(f"Added participant for {name} on {date}")
    else:
        event = Event(name, date) # adds an event and adds the participant
        event.add_participant()
        participants[event_pair] = event
        print(f"Added participant for {name} on {date}")

def get_count():
    for event in participants.values():
        event.display_count()

while True:
    try:
        print("Welcome to the Event Management system")
        option = input("To add participant enter 'add', to get a head count enter 'count', or 'quit': ").lower()
        if option == "add":
            name = input("Enter event name: ")
            date = input("Enter event date: ")
            add_count(name, date)
        elif option == "count":
            if participants:
                get_count()
            else:
                print("No participants have RSVP'd")
        elif option == "quit":
            break
    except Exception as e:
        print(f"Error message '{e}'. Please try again")
    

