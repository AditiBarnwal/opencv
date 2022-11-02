# opencv

**open-source library for COMPUTER VISION, ML, and IMAGE PROCESSING.** 

👩 It can process images and videos to identify objects, faces, or even the handwriting of a human.

***When it is integrated with various libraries, such as Numpy which is a highly optimized library for numerical operations, 
then the number of weapons increases in your Arsenal i.e whatever operations one can do in Numpy can be combined with OpenCV.***

## Introduction

Computer vision is a process by which we can understand the images and videos how they are stored and how we can manipulate and retrieve data from them. Computer 
Vision is the base or mostly used for Artificial Intelligence. Computer-Vision is playing a major role in self-driving cars, robotics as well as in photo correction 
apps. 

About OpenCV 👆

#### Applications of OpenCV: 
There are lots of applications which are solved using OpenCV, some of them are listed below 

            🌜     face recognition

            🌜     Automated inspection and surveillance
            
            🌜     number of people – count (foot traffic in a mall, etc)
            
            🌜     Vehicle counting on highways along with their speeds
            
            🌜     Interactive art installations
            
            🌜     Anomaly (defect) detection in the manufacturing process (the odd defective products)
            
            🌜     Street view image stitching
            
            🌜     Video/image search and retrieval
            
            🌜     Robot and driver-less car navigation and control
            
            🌜     object recognition
            
            🌜     Medical image analysis
            
            🌜     Movies – 3D structure from motion
            
            🌜     TV Channels advertisement recognition
    
    
    #### OpenCV Functionality 
 
🎶  Image/video I/O, processing, display (core, imgproc, highgui)

🎶  Object/feature detection (objdetect, features2d, nonfree)

🎶  Geometry-based monocular or stereo computer vision (calib3d, stitching, videostab)

🎶  Computational photography (photo, video, superres)

🎶  Machine learning & clustering (ml, flann)

🎶  CUDA acceleration (gpu)

***Image-Processing***

Image processing is a method to perform some operations on an image, in order to get an enhanced image and or to extract some useful information from it. 
If we talk about the basic definition of image processing then “Image processing is the analysis and manipulation of a digitized image, 
especially in order to improve its quality”. 
- Digital-Image : 

An image may be defined as a two-dimensional function f(x, y), where x and y are spatial(plane) coordinates, and the amplitude of fat any pair of coordinates (x, y) 
is called the intensity or grey level of the image at that point. 
In another word An image is nothing more than a two-dimensional matrix (3-D in case of coloured images) which is defined by the mathematical function f(x, y) 
at any point is giving the pixel value at that point of an image, the pixel value describes how bright that pixel is, and what colour it should be. 
Image processing is basically signal processing in which input is an image and output is image or characteristics according to requirement associated with that image. 

Image processing basically includes the following three steps: 
 
~ Importing the image

~ Analysing and manipulating the image

~ Output in which result can be altered image or report that is based on image analysis

💭 How Does A Computer Read An Image? 
We are humans we can easily make it out that the image of a person who is . But if we ask computer “is it my photo?”.The computer can’t say anything because
the computer is not figuring out it all on its own. The computer reads any image as a range of values between 0 and 255. For any color image, 
there are 3 primary channels -red, green and blue.

## Working with Images

Most basic and important concepts of OpenCV:

***Reading an image***
      ` # Reading the image using imread() function`
      
      `image = cv2.imread('image.png')`
      
      `# Extracting the height and width of an image`
      
      `h, w = image.shape[:2]`
      
      `# Displaying the height and width`
      
      `print("Height = {},  Width = {}".format(h, w))`

***Extracting the RGB values of a pixel***

          `# Extracting RGB values. `

          `# Here we have randomly chosen a pixel`
    
          `# by passing in 100, 100 for height and width.`

           `(B, G, R) = image[100, 100]`
  
           `# Displaying the pixel values`

           `print("R = {}, G = {}, B = {}".format(R, G, B))`
  
           `# We can also pass the channel to extract `

           `# the value for a specific channel`

           `B = image[100, 100, 0]`

           `print("B = {}".format(B))`

***Extracting the Region of Interest (ROI)***
      
      `#calculate the region of interest `
      
      `# by slicing the pixels of the image`
      
      `roi = image[100 : 500, 200 : 700]`

***Resizing the Image***

         ` # resize() function takes 2 parameters, `

          `# the image and the dimensions`

          `resize = cv2.resize(image, (800, 800))`

***Rotating the Image***
         `# Calculating the center of the image`
         
         `center = (w // 2, h // 2)`
  
         `# Generating a rotation matrix`
         
         `matrix = cv2.getRotationMatrix2D(center, -45, 1.0) `
  
         `# Performing the affine transformation`
          
          `rotated = cv2.warpAffine(image, matrix, (w, h))`
          There are a lot of steps involved in rotating an image.The 2 main functions used here are –

                 - getRotationMatrix2D()
                 - warpAffine()
                 
***Drawing a Rectangle***

***Displaying text***

## Getting Started

#### cv2.imshow()
method is used to display an image in a window. The window automatically fits to the image size.
 
Syntax: `cv2.imshow(window_name, image)`
         Parameters: 
         - window_name: A string representing the name of the window in which image to be displayed. 
         - image: It is the image that is to be displayed.
         - Return Value: It doesn’t returns anything. 

#### cv2.imwrite() 
method is used to save an image to any storage device. This will save the image according to the specified format in current working directory.

Syntax: `cv2.imwrite(filename, image)`

            Parameters:
            - filename: A string representing the file name. The filename must include image format like .jpg, .png, etc.
            - image: It is the image that is to be saved.

            ~ Return Value: It returns true if image is saved successfully.
 ***Color spaces are a way to represent the color channels present in the image that gives the image that particular hue.        ***

**Arithmetic Operations on Images using OpenCV | Set-1 (Addition and Subtraction)        **
 
 ***cv2.add()***. This directly adds up image pixels in the two images. 
                 Syntax: `cv2.add(img1, img2)`

But adding the pixels is not an ideal situation. So, we use cv2.addweighted(). Remember, both images should be of equal size and depth. 
 

                 Syntax: `cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)`

Parameters: 
                 - img1: First Input Image array(Single-channel, 8-bit or floating-point) 
                 - wt1: Weight of the first input image elements to be applied to the final image 
                 - img2: Second Input Image array(Single-channel, 8-bit or floating-point) 
                 - wt2: Weight of the second input image elements to be applied to the final image 
                 - gammaValue: Measurement of light

subtract the pixel values in two images and merge them with the help of ***cv2.subtract()***. The images should be of equal size and depth. 
 
                         Syntax:  `cv2.subtract(src1, src2)`
       
       
**Bitwise operations** are used in image manipulation and used for extracting essential parts in the image. In this article, Bitwise operations used are : 
                  `AND`                             `OR`                             `XOR`                          `NOT`

Also, Bitwise operations helps in image masking. Image creation can be enabled with the help of these operations. These operations can be helpful in enhancing the properties of the input images. 

NOTE: The Bitwise operations should be applied on input images of same dimensions
  
  ![SYNTAX](https://www.geeksforgeeks.org/arithmetic-operations-on-images-using-opencv-set-2-bitwise-operations-on-binary-images/)
## Image Processing

Image Resizing

Eroding an Image

Blurring an Image

Create Border around Images

Grayscaling of Images

Scaling, Rotating, Shifting and Edge Detection

Erosion and Dilation of images

Analyze an image using Histogram

Histograms Equalization

Simple Thresholding

Adaptive Thresholding

Otsu Thresholding

Segmentation using Thresholding

Convert an image from one color space to another

Filter Color with OpenCV

Denoising of colored images

Visualizing image in different color spaces

Find Co-ordinates of Contours

Bilateral Filtering

Image Inpainting using OpenCV

Intensity Transformation Operations on Images

Image Registration

Background subtraction

Background Subtraction in an Image using Concept of Running Average

Foreground Extraction in an Image using Grabcut Algorithm

Morphological Operations in Image Processing (Opening)

Morphological Operations in Image Processing (Closing)

Morphological Operations in Image Processing (Gradient)

Image segmentation using Morphological operations

Image Translation

Image Pyramid

## Feature Detection and Description

1.Line detection using Houghline method
2.Circle Detection
3.Detect corner of an image
4.Corner Detection with Shi-Tomasi method
5.Corner detection with Harris Corner Detection
6.Find Circles and Ellipses in an Image
7.Document field detection
8.Smile detection

## Drawing Functions

     🔆     Draw a line
     🔆     Draw arrow segment
     🔆     Draw an ellipse
     🔆     Draw a circle
     🔆     Draw a rectangle
     🔆     Draw a text string
     🔆     Find and Draw Contours
     🔆     Draw a triangle with centroid
## Working with Videos
## Getting Started
## Video Processing

## Extra

💭 Why OpenCV is used in image processing?

OpenCV is the huge open-source library for the computer vision, machine learning, and image processing and now it plays a major role in real-time
operation which is very important in today's systems. By using it, one can process images and videos to identify objects, faces, or even handwriting of a human.

💭 Is OpenCV related to image processing?

Image result for difference between Image processing and opencv
OpenCV is a pre-built, open-source CPU-only library (package) that is widely used for computer vision, machine learning, and image processing applications.
