# Controlone.ai_Assignement

This README file provides a brief overview of three code snippets provided as the Assignments purpose.

## Code 1: Face Detection with OpenCV

#### Description
The first code snippet is used for real-time face detection using OpenCV and a pre-trained Haar Cascade classifier. It captures video from the default camera (usually the webcam) and draws rectangles around detected faces in real-time.

#### Instructions
- Make sure you have OpenCV installed.
```bash
  pip install opencv-python
  pip insatll cv2
```
- Download the "haarcascade_frontalface_default.xml" classifier and place it in the same directory as the script. (The file is already there.)
```bash
  https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
```
- Run the script.
- Press 'q' to exit the application.

## Code 2: Drawing Geometric Shapes with OpenCV
#### Description
The second code snippet demonstrates how to draw various geometric shapes on a blank canvas using OpenCV. It creates an image with lines, rectangles, ellipses, and circles, and displays it.

#### Instructions
Ensure you have OpenCV installed.
Run the script to display the image with geometric shapes.
Close the window by pressing any key.

#### Screenshot 
![shape](https://github.com/AdityaSaxena1311/Controlone.ai_Assignement/assets/80876781/3383f8d0-c12b-4ac1-a9aa-0183ac5710f5)


## Code 3: Warehouse Parcel Detail Processing
#### Description
The third code snippet is designed to process warehouse parcel details from a CSV file, categorize them, and save the categorized data into a new CSV file. It also displays the categorized data in a tabular format.

#### Instructions
Create a CSV file named "data.csv" with parcel details (Parcel Number, Parcel Weight, Parcel Category).
Run the script.
It will categorize the parcels, display them in a tabular format, and save the categorized data in "parcel_details.csv."
