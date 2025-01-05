# Drone Precsion Landing using visual odometry
This project focuses on a precision landing algorithm for drones, leveraging computer vision techniques. The algorithm is designed to detect ArUco markers captured by the drone's camera, enabling accurate localization of the landing target.
Once the ArUco marker is detected, the drone locks onto its position and adjusts its flight path to ensure a smooth and precise landing. The algorithm combines real-time marker detection, position estimation, and control adjustments, ensuring robustness even in dynamic environments.
This system is ideal for applications requiring autonomous drone operations, such as package delivery, industrial inspections, or emergency response, offering a reliable and efficient solution for precision landing tasks.

## Quadrotor Dynamics 
![image](https://github.com/user-attachments/assets/963d1576-d6be-438f-872d-4a2267ac2972)
* Total Degree of freedom of the system is DOF=6.
* Total Number of inputs are in the system is U=4.
*	As U < DOF the drone lies in the underactuated system

Reference drone configuration taken as follows.
* X axis pointing towards earths north surface
* Y axis pointing towards East
* Z axis pointing towards the earth centre

![image](https://github.com/user-attachments/assets/21d7e882-2051-49ca-82dd-e9781ac78a53)

* From the Drone dynamics the values and reading are getting with respect to the body of the system
* As Flight controller usually works based on the Newtons law of motion for physical parameter calculation
* The Newtons law of motion is only valid in Inertia frame of reference.
* Euler angle transformation to transform a parameter from Body to inertia reference frame.

![image](https://github.com/user-attachments/assets/0b499f4d-a74d-4c1b-a1c0-9d86ef142584)

When we are transforming from the Inertia to Body Frame of reference The Rotation matrix of each axis should multiply in the correct sequence.
* First about Yaw axis
*	Then pitch axis.
*	Then Roll axis.
![image](https://github.com/user-attachments/assets/c74107a4-a006-4229-ae6a-367fb9ba13c1)

Same as linear motion we can compute for the rotational motion.
![image](https://github.com/user-attachments/assets/27a0c963-307b-44c8-8720-bc94bc945261)

## Equation of motion
![image](https://github.com/user-attachments/assets/709959bf-ea12-4637-bbd9-79e6a12ba6bd)



## Camera calibration
![Flowchart](https://github.com/Praveenkottari/vision-based-drone-softlanding/blob/7c82fed178abad07ed64d30cd849d8148403b23e/pics/MicrosoftTeams-image%20(6).png)

## Drone setup and Hardware
  * PX4 Autopilot
  * Radio control
  * Raspberry Pi
  * Raberry pi camera

## Acknowledgements

 - [Ground Pattern Recognition]([https://www.mdpi.com/2079-9292/8/12/1532])
 - [SkYnSPACE](https://github.com/SKYnSPACE?tab=repositories)
