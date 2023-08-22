# Lane-Guiding-Robot
This lane guiding robot is powered by a Raspberry Pi 4B, contains an integrated expansion board as a chassis, a high definition camera, four TT DC motors and multiple other components that make the lane guidance module possible.
This is a project built for my bachelors degree of Computer Science, and it contain different Artificial Intelligence implementations such as Object Detection, Deep Learning, Computer Vision, etc.
The robot must stay within the drawn lane, just like in a real life scenario, using the techniques mentioned above to calculate the error needed for steering left and right. 
Moreover, I have also implemented a cascade classifier that utilises a pre-generated xml file of stop signs, to detect stop signs whilst the robot is navigating on the track.
If a stop sign is the detected, the robot shall simulate a full brake for 5 seconds, and continue navigating down the predefined path afterwards.
