'use strict';

/* A Toy Event Machine 
@author - Ankur Anand
Tested Using Nodejs 6.2*/

// Event
class Event	{
	// Structure of Event Object
	constructor (etype, data){
		this.etype = etype; // event type
		this.data = data; // data associated with the event
	}

	toString() {
		// toString representation of object
		return `(${this.etype}, ${this.data})`;
	}
}

// Event Handler
function eventHandler_A (event) {
	// Handle Event of type A
	if 	( ! event instanceof Event ){
		console.log('Not an Event Object');
	}
	else {
		console.log(`Event of type ${event.etype} occurred with Data 
			${event.data}`);
	}
	
}

function eventHandler_B(event) {
	// Handle Event of type B
	if ( ! event instanceof Event ){
		console.log('Not an Event Object');
	}
	else {
		console.log(`Event of type ${event.etype} occurred with Data 
			${event.data.toUpperCase()}`);
	}
}


class Queue {
	// A queue class for storing Events FIFO
	constructor (){
		this.items = [];
	}

	// methods acting on the queue
	isEmpty() {
		return (this.items).length === 0;
	}

	enqueue(item) {
		// push at the beginning of the array
		this.items.unshift(item);
	}

	dequeue(item) {
		// pop the last element
		return this.items.pop();
	}

	size() {
		return (this.items).length;
	}
	
}


let events = new Queue();
events.enqueue(new Event('A','Hello'));
events.enqueue(new Event('B', 'Event-Driven'));
events.enqueue(new Event('A', 'World'));


let handler_dispatcher = {
	'A' : eventHandler_A,
	'B' : eventHandler_B
}
// Event loop
while (! events.isEmpty()) {
	let e = events.dequeue();
	/*if ( e.etype === 'A') {
		eventHandler_A(e);
	}
	if ( e.etype === 'B') {
		eventHandler_B(e);
	}*/

	handler_dispatcher[e.etype](e);
}
