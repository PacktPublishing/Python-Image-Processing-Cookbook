## $5 Tech Unlocked 2021!
[Buy and download this Book for only $5 on PacktPub.com](https://www.packtpub.com/product/python-image-processing-cookbook/9781789537147)
-----
*If you have read this book, please leave a review on [Amazon.com](https://www.amazon.com/gp/product/1789537142).     Potential readers can then use your unbiased opinion to help them make purchase decisions. Thank you. The $5 campaign         runs from __December 15th 2020__ to __January 13th 2021.__*

# Python Image Processing Cookbook

<a href="https://www.packtpub.com/data/python-image-processing-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781789537147"><img src="https://www.packtpub.com/media/catalog/product/cache/e4d64343b1bc593f1c5348fe05efa4a6/9/7/9781789537147-original.jpeg" alt="Python Image Processing Cookbook" height="256px" align="right"></a>

This is the code repository for [Python Image Processing Cookbook](https://www.packtpub.com/data/python-image-processing-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781789537147), published by Packt.

**Over 60 recipes to help you perform complex image processing and computer vision tasks with ease**

## What is this book about?
Advancements in wireless devices and mobile technology have enabled the acquisition of a tremendous amount of graphics, pictures, and videos. Through cutting edge recipes, this book provides coverage on tools, algorithms, and analysis for image processing. This book provides solutions addressing the challenges and complex tasks of image processing.

This book covers the following exciting features: 
* Implement supervised and unsupervised machine learning algorithms for image processing
* Use deep neural network models for advanced image processing tasks
* Perform image classification, object detection, and face recognition
* Apply image segmentation and registration techniques on medical images to assist doctors
* Use classical image processing and deep learning methods for image restoration
* Implement text detection in images using Tesseract, the optical character recognition (OCR) engine
* Understand image enhancement techniques such as gradient blending

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/B084ZN7Y5F) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example,

The code will look like the following:
```
def get_grid_coordinates(points):
  xmin, xmax = np.min(points[:, 0]), np.max(points[:, 0]) + 1
  ymin, ymax = np.min(points[:, 1]), np.max(points[:, 1]) + 1
  return np.asarray([(x, y) for y in range(ymin, ymax)
         for x in range(xmin, xmax)], np.uint32)

```

**Following is what you need for this book:**
This book is for image processing engineers, computer vision engineers, software developers, machine learning engineers, or anyone who wants to become well-versed with image processing techniques and methods using a recipe-based approach. Although no image processing knowledge is expected, prior Python coding experience is necessary to understand key concepts covered in the book.

With the following software and hardware list you can run all code files present in the book.

### Software and Hardware List

| Chapter  | Software required                                                                         | OS required                        |
| -------- | ------------------------------------------------------------------------------------------| -----------------------------------|
| 1 - 9    | Python 3.7, Anaconda version 2019.10 (py37_0), GPU (if available)                         | Windows, Mac OS X, and Linux (Any) |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781789537147_ColorImages.pdf).


### Related products <Other books you may enjoy>
* Hands-On Image Processing with Python [[Packt]](https://www.packtpub.com/big-data-and-business-intelligence/hands-image-processing-python?utm_source=github&utm_medium=repository&utm_campaign=9781789343731) [[Amazon]](https://www.amazon.com/dp/B07J664F9S)

* PyTorch Computer Vision Cookbook [[Packt]](https://www.packtpub.com/in/data/pytorch-computer-vision-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781838644833) [[Amazon]](https://www.amazon.com/dp/1838644830)

## Get to Know the Authors
**Sandipan Dey**
is a data scientist with a wide range of interests, covering topics such as machine learning, deep learning, image processing, and computer vision. He has worked in numerous data science fields, working with recommender systems, predictive models for the events industry, sensor localization models, sentiment analysis, and device prognostics. He earned his master's degree in computer science from the University of Maryland, Baltimore County, and has published in a few IEEE Data Mining conferences and journals. He has earned certifications from 100+ MOOCs on data science, machine learning, deep learning, image processing, and related courses. He is a regular blogger (sandipanweb) and is a machine learning education enthusiast.


### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSdy7dATC6QmEL81FIUuymZ0Wy9vH1jHkvpY57OiMeKGqib_Ow/viewform) if you have any feedback or suggestions.
