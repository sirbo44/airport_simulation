This is an airport simulation python program
We use a priority queue for landings and a simple one for takeoffs 

To run your own cases change code below line 123 and within the if statement 

Create a landing queue using this command```NAME_OF_THE_LANDING_QUEUE = LandingQueue()```
Create a takeoff queue using this command```NAME_OF_THE_QUEUE = TakeoffQueue()```

To request normal landing use this command ```NAME_OF_THE_LANDING_QUEUE.landing_request("NAME_OF_THE_FLIGHT", 0)```

To request emergency landing use this command ```NAME_OF_THE_LANDING_QUEUE.landing_request("NAME_OF_THE_FLIGHT", 100)```

To land use this command ```NAME_OF_THE_LANDING_QUEUE.land()```

To request takeoff use this command ```NAME_OF_THE_TAKEOFF_QUEUE.takeoff_request("NAME_OF_THE_FLIGHT")```

To takeoff use this command ```NAME_OF_THE_TAKEOFF_QUEUE.takeoff()```