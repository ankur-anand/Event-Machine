#################################
### A Toy Event machine 	#####
### @author - Ankur Anand	#####
### Tested using python 3.5.2 ###
#################################


### Event
class Event(object):
	""" Structure for event object"""
	def __init__(self, etype, data):
		self.etype = etype # type of the event
		self.data = data # data associated with the type events

	def __str__(self):
		""" String representation of the class instance """
		return 'Event({etype}, {data})'.format(
				etype = self.etype,
				data = repr(self.data)
			)
	def __repr__(self):
		return self.__str__()


####### Event Handlers. In our toy implementation we are defining two event
####### handlers A and B

def eventHandler_A(event):
	""" receives a event of type A and print it"""
	if not type(event) is Event:
		print("Not an Event")
	print("Event Type A Occurred with data : ",event.data)

def eventHandler_B(event):
	""" receives a event of type B and uppercase it data"""
	if not type(event) is Event:
		print("Not an Event")
	print("Event Type B Occurred with data : ", (event.data).upper()) 



########### Implementing a Queue to store events ###

class Queue(object):
	""" A FIFO Queue"""
	def __init__(self):
		self.items = []

	def isEmpty(self):
		""" return True if the Queue is empty"""
		return self.items == []

	def enqueue(self, item):
		""" Add the element at the beginning of Queue """
		self.items.insert(0, item)

	def dequeue(self):
		""" Remove the element from Queue from the last"""
		return self.items.pop()

	def size(self):
		""" Return the size of the Queue"""
		return len(self.items)



events = Queue()
events.enqueue(Event('A','Hello'))
events.enqueue(Event('B','event-driven'))
events.enqueue(Event('A','world'))

### Event Loop
while not events.isEmpty():
	e = events.dequeue()
	if e.etype == 'A':
		eventHandler_A(e)
	if e.etype == 'B':
		eventHandler_B(e)


##### OutPut ######
"""
Event Type A Occurred with data :  Hello
Event Type B Occurred with data :  EVENT-DRIVEN
Event Type A Occurred with data :  world
"""
