# B.S Computer Vision Project 
# Real-Time Facial Expression Recognition

### Used Dataset to train Ml Model
Cohn-Kanade dataset http://www.consortium.ri.cmu.edu/ckagree/

### Used Algorithm 

1)Haar-feature basedcascade classifiers to detect faces and algorithms
2)Fisherface” algorithm

### Image Pre-processing

Although the face cascade is very useful for recognition, we needed all faces to be upright and centered on the image. 
If the head is not straight then it may cause problems. In order to compensate for the head orientation, we will rotate and scale to the image so that all faces will be perfectly aligned.In other words, during preprocessing we used affine transformations.

Rotation: Firstly, we detected both right and left eye separately. Then, calculated the angle between the line that connects the center of both eyes and horizon to rotate the face accordingly.
Scaling: We want all faces to be in the center. So, we want the eyes to to be precisely at 25% and 75% of the image width and 20% of the image height.

After calculating rotation and scaling matrices, we applied affine transformation by warpAffine function.Furthermore, we cropped each face as a square shape.
 
### Result Example
https://github.com/ebocugoz/Sabanci-Computer-Vision-Project/blob/master/Report/sad.png

![alt text](https://raw.githubusercontent.com/ebocugoz/Sabanci-Computer-Vision-Project/blob/master/Report/sad.png)

![alt text](https://raw.githubusercontent.com/ebocugoz/Sabanci-Computer-Vision-Project/master/Report/surprise.png)

