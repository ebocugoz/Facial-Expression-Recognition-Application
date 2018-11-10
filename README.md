
# Real-Time Facial Expression Recognition

### Used Dataset to train Ml Model
Cohn-Kanade dataset http://www.consortium.ri.cmu.edu/ckagree/

### Used Algorithm 

1)Haar-feature basedcascade classifiers to detect faces and algorithms
2)Fisherface” algorithm

### Image Pre-processing

Although the face cascade is very useful for recognition, all faces need to be upright and centered on the image. 
If the head is not straight then it may cause problems. In order to compensate for the head orientation, images are rotated and scaled  so that all faces will be perfectly aligned.In other words, during preprocessing affine transformations are used.

Rotation: Firstly, both right and left eye detected separately using haar-cascade. Then, calculated the angle between the line that connects the center of both eyes and horizon to rotate the face accordingly.
Scaling: All faces should be in the center. So,  the eyes need be precisely at 25% and 75% of the image width and 20% of the image height.

After calculating rotation and scaling matrices,  affine transformation is applied by warpAffine function.Furthermore, we cropped each face as a square shape.
 
### Result Example

![Surprise](https://github.com/ebocugoz/Sabanci-Computer-Vision-Project/blob/master/Report/surprise.png)

![Sad](https://github.com/ebocugoz/Sabanci-Computer-Vision-Project/blob/master/Report/sad.png)
