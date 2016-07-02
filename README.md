# Toy event-machine
A very basic simple event machine written in python and javascript for learning purpose

##Fundamental Component of Event-Driven Architecture
1. Events - an occurrence to handle
2. Event-Handlers - a method to handle the occurrence
3. Event Loop - an continuous loop to maintain interaction between events and event-handlers

Flow - Events are sent to the Event-loop which dispatches the event to their respective
event handlers

### Events:
Events are the heart of the Event Driven Architecture. It consists of two necessary properties
1. type - type determines which handlers to handle the events
2. data - data used by the handler

pseudo model of Events

```
class Event:
	constructor(type,data):
		self.type = type
		self.data = data
	
```

### Event-Handlers:
Handlers are specific way to deal with an events, i.e what operation to perform on the data on occurrence of the specified type event.

pseudo model of Handlers
```
function handlerA(Event e):
	print "event A occurred with e.data"
```

### Event Loop:
This process all events as they arrive by dispatching them to their respective
handlers until a terminating condition occurs	
