# Drone Precsion Landing using visual odometry
This project focuses on a precision landing algorithm for drones, leveraging computer vision techniques. The algorithm is designed to detect ArUco markers captured by the drone's camera, enabling accurate localization of the landing target.
Once the ArUco marker is detected, the drone locks onto its position and adjusts its flight path to ensure a smooth and precise landing. The algorithm combines real-time marker detection, position estimation, and control adjustments, ensuring robustness even in dynamic environments.
This system is ideal for applications requiring autonomous drone operations, such as package delivery, industrial inspections, or emergency response, offering a reliable and efficient solution for precision landing tasks.
![image](https://github.com/Praveenkottari/vision-based-drone-softlanding/blob/591b1e55e92710c97dcb1e70370253d033f9ef9b/pics/MicrosoftTeams-image%20(8).png)


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

These equations are representing the translational dynamics of a quadrotor drone, describing how the drone's orientation affects its movement in the three-dimensional space. The X and Y equations account for the drone's motion in the horizontal plane (X and Y axes), factoring in the combined effects of the drone's roll (ϕ), pitch (θ), and yaw (ψ) on the thrust force (Tx ) generated by the rotors. These equations illustrate that the drone's movement along each axis is a function of its orientation and the distribution of thrust among its rotors. The Z equation describes vertical motion (along the Z-axis), incorporating the effects of the drone's attitude on the vertical thrust component while also considering the gravitational force (g). The negative signs in front of the thrust terms signify that the thrust force produced by the rotors is oriented in the opposite direction to the drone's acceleration. Collectively, these equations are pivotal for designing control algorithms that enable a drone to navigate to a specific point autonomously and accurately in space, essential for tasks such as precision landing or aerial manoeuvres.

## Aruco marker
An ArUco marker is a synthetic square marker composed by a wide black border and Inner binary matrix that encodes the marker's ID and that is used extensively in computer vision applications, especially for pose estimation and augmented reality tasks. The size of this matrix can vary, commonly being 4x4, 5x5, 6x6, or 7x7. The binary pattern is what makes each marker unique. The matrix consists of black and white squares, where black typically represents a '0' and white represents a '1’. In inner matrix odd columns are represents the parity bits even columns contain data bits. Their simplicity and robustness to various lighting conditions and perspectives make them particularly useful for real-time applications. The maximum number of markers that can be encoded is 22n where n-number of data Coloum.

In the context of UAVs, ArUco markers can serve as precise reference points for navigation and landing. When an onboard camera captures an image containing a marker, computer vision algorithms can determine the position and orientation of the UAV in relation to the marker. This is essential for applications where precision is crucial, such as automated landing processes where the UAV must align itself correctly with a charging pad or landing platform. The advantage of using ArUco markers lies in their ease of use and the low computational resources required for processing. They can be generated in any size and printed on a variety of materials, which allows for flexible deployment in different environments. Moreover, they are supported by multiple computer vision libraries, including OpenCV, which provides pre-built functions for detecting and estimating the pose of markers in each image. This makes ArUco markers a cost-effective and efficient solution for enhancing the capabilities of UAVs and other computer vision-based systems.

## Object detection
For object detection from the Raspberry pi camera, we have feed the camera images to precision landing algorithm. ArUco markers detection process must return a list of detected markers. Each detected marker includes.
*	The position of its four corners in the image 
*	The id of the marker
  
![image](https://github.com/user-attachments/assets/774b69ca-2cf0-4a77-a47a-6be46b812e2c)

In the Detection of marker step the image is analysed to find square shapes that are candidates to be markers. It begins with an adaptive thresholding to segment the markers, then contours are extracted from the thresholder image and those that are not convex or do not approximate to a square shape are discarded. After the candidate detection, it is necessary to determine if they are markers by analysing their inner codification. This step starts by extracting the marker bits of each marker. To do so, a perspective transformation is first applied to obtain the marker in its canonical form. Then, the canonical image is thresholder using Otsu to separate white and black bits. The image is divided into different cells according to the marker size and the border size. Then the number of black or white pixels in each cell is counted to determine if it is a white or a black bit. Finally, the bits are analysed to determine if the marker belongs to the specific dictionary. Error correction techniques are employed when necessary.


## Camera calibration
Once the camera is installed to the pi we need to calibrate the camera. Camera calibration is an essential step before performing tasks such as object recognition, and it becomes even more crucial when dealing with precision tasks like detecting ArUco markers with a Raspberry Pi camera. Calibration is used to correct lens distortion and find the intrinsic and extrinsic parameters of the camera.
Calibration methods rely on one or more images of a calibration pattern: 
(1) a 3D object of known geometry. 
(2) it is in a known position in space. 
(3) it is generating image features which can be located accurately


<p align="center">
    <img src="https://github.com/user-attachments/assets/6287320f-16da-4e40-a6a0-d779f18caaf6"  width="400" style="margin-right: 50px;"/>
    <img src="https://github.com/user-attachments/assets/b7f0d554-0390-4fa7-a86d-f541622edc5b"  width="400" style="margin-left: 50px;"/>
</p>
<p align="center">
    <img src="https://github.com/Praveenkottari/vision-based-drone-softlanding/blob/7c82fed178abad07ed64d30cd849d8148403b23e/pics/MicrosoftTeams-image%20(6).png"  width="400" style="margin-right: 50px;"/>
    <img src="https://github.com/user-attachments/assets/eecfab39-c875-44c5-a4bb-a9518e797d1f"  width="400" style="margin-left: 50px;"/>
</p>

- The precision of calibration depends on how accurately the world and image points are located. 
- Studying how localization errors "propagate" to the estimates of the camera parameters is very important. 

## Camera Integration and Landing
	The system continuously captures images using an onboard camera These images are processed in real-time to detect the presence of a predefined marker Once the target marker is identified in the camera's view algorithm analyses its orientation and position This analysis often involves calculating the marker's distance and angle relative to the camera to determine the vehicle's position relative to the landing zone The system uses the positional data of the marker to adjust the vehicle's alignment and position. If necessary, code will allow the vehicle manoeuvres to align itself directly above the marker, ensuring a safe landing trajectory.
![image](https://github.com/user-attachments/assets/40a2fc12-6bd6-423e-9258-28b014842d95)


## Drone setup and Hardware
  * PX4 Autopilot
  * Radio control
  * Raspberry Pi
  * Raberry pi camera

## Acknowledgements

 - [Ground Pattern Recognition]([https://www.mdpi.com/2079-9292/8/12/1532])
 - [SkYnSPACE](https://github.com/SKYnSPACE?tab=repositories)
