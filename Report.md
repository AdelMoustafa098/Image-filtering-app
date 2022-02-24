| Submitted to | Prof/ Ahmed M. Badawi |  |  |
| ----------- | ----------- | ----------- | ----------- |
| **By** | - Adel Moustafa | Sec: 2 | Bn: 3 |
|     | - Omar Ibrahim | Sec: 2 | Bn: 9 |
|     | - Mohamed Yasser | Sec: 2 | Bn: 24 |
| | - Mahmoud Abdelrhman | Sec: 2 | Bn: 25 |
| **Group ID** | 19 |  |  |

------

[TOC]

------

# Overview of the task

This project consists of 3 modules:  
1-**main.py**  : main program  
2-**GUI.py** : Pyqt GUI script  
3-**func.py** : contains the implementation of the used functions  

	
------

# Program description

- **From** file, **choose** load image "choose only 1 image".

- **From** noise combo-box, **choose** a type of noise.

- Then, **From** filter combo-box, **choose** a filter type that will process the noisy image.

- **From** edge combo-box, **choose** a type of edge detector that will process the original image.

- **From** more, you can **choose** any option you like and a pop-up window will be shown to choose an image and the specified option will be applied.

  `Note`: keep in mind that for Hyprid image you have to choose 2 images or the Hyprid image option will not work.

------

# Results

- Salt and Pepper noise and (5x5) Gaussian filter

  ![](Result_images\1.png)

- Salt and Pepper noise and (5x5) Average filter

  ![](Result_images\2.png)

- Salt and Pepper noise and (3x3) Median filter

  ![](Result_images\3.png)

- Gaussian noise and (5x5) Average filter

  ![](Result_images\4.png)

- Gaussian noise and (5x5) Gaussian filter

  ![](Result_images\5.png)

- Gaussian noise and (3x3) Median filter

  ![](Result_images\6.png)

- Uniform noise and (5x5) Average filter

  ![](Result_images\7.png)

- Uniform noise and (5x5) Gaussian filter

  ![](Result_images\8.png)

- Uniform noise and (5x5) Median filter

  ![](Result_images\9.png)

- Sobel edge detection

  ![ ](Result_images\10.png)

- Roberts edge detection

  ![](Result_images\11.png)

- Prewitt edge detection

  ![](Result_images\12.png)

- Canny edge detection

  ![](Result_images\13.png)

- Convert Image to grayscale and show grayscale Histogram

  ![](Result_images\14.png)

- RGB Histogram

  ![](Result_images\15.png)

- Image Equalization

  ![](Result_images\16.png)

- Image Normalization

  ![](Result_images\17.png)

- Hybrid Image

  ○   Gaussian filter for the first input

  ○   Laplacian filter for the second input

  ![](Result_images\18.png)

- Frequency domain filter (Low pass filter)

  ![](Result_images\19.PNG)

- 20- Frequency domain filter (High pass filter)

  ![](Result_images\20.png)

- Global threshold

  ![](Result_images\21.jpeg)

- Local threshold

  ![](Result_images\22.jpeg)

- Global threshold doesn't usually show good outputs compared to local threshold

  ![](Result_images\23.jpeg)

  

