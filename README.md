# blind_people_assister

This is created to solve problem faced by blind people for navigation in the environment.

We used 2 esp-cam and perform stereo vision from it to get an depth map with relatively accurate results and then used state of the art yolo model to get the label of the object present in the environment . Then combine both the results and used them to navigate the user via audio output.
