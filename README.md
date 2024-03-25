This is an airport simulation python program<br>
We use a priority queue for landings and a simple one for takeoffs <br>

To run your own cases change code below line 123 and within the if statement <br>

Create a landing queue using this command```NAME_OF_THE_LANDING_QUEUE = LandingQueue()```<br>
Create a takeoff queue using this command```NAME_OF_THE_QUEUE = TakeoffQueue()```<br>

To request normal landing use this command ```NAME_OF_THE_LANDING_QUEUE.landing_request("NAME_OF_THE_FLIGHT", 0)```<br>

To request emergency landing use this command ```NAME_OF_THE_LANDING_QUEUE.landing_request("NAME_OF_THE_FLIGHT", 100)```<br>

To land use this command ```NAME_OF_THE_LANDING_QUEUE.land()```<br>

To request takeoff use this command ```NAME_OF_THE_TAKEOFF_QUEUE.takeoff_request("NAME_OF_THE_FLIGHT")```<br>

To takeoff use this command ```NAME_OF_THE_TAKEOFF_QUEUE.takeoff()```<br>
