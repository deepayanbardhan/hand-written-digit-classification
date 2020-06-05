## Hand Written Digit Classification

![Python 3.6](https://img.shields.io/badge/Python-3.6-brightgreen.svg)    ![Problem Kaggle](https://img.shields.io/badge/Problem-Vision-blue.svg)     ![Problem Kaggle](https://img.shields.io/badge/Data-Kaggle-orange.svg)
<center>
<img src="/images/lhwdc/hwdc.gif" alt="centered image" width="350">
 </center>
<p style = "font-weight: 400; font-size: 15px;" align="justify">Hand written text classification is one of the basic problems in the field of Machine Learning. There has been so many techniques developed for the task for example ANN, Perceptron modelling and many more. But one of the most common architecture that has been able to perform much better than most of the other ML architectures is CNN. Convolutional Neural Networks, commonly known as CNN, are very popular when it comes to pattern recognition and image analysis because of its ease of use and the results that they produce. </p>

<div style = "font-weight: 400; font-size: 15px;">
In this particular project, I have tried to perform 2 specific tasks:
  <ul>
    <li> Demonstrate the working of CNN and its performance</li>
    <li> Identify a digit from an image or live camera</li>
  </ul>
</div>

<div style = "font-weight: 400; font-size: 15px;">
   <h3> Implementing and Demonstrating CNN: </h3>
    <p style = "font-weight: 400; font-size: 15px;" align="justify"> Here I have built a CNN model using Keras framework. The Keras framework allows us to build a CNN model very easily. It has been demonstrated how a CNN model actaully classifies an image in its respective class or what does a layer in CNN sees when it gets certain images. The details can be checked in <a href="https://www.kaggle.com/dbardhan/beginners-guide-to-cnns-99-47" style="text-decoration:none;">my notebook code</a>. The model has been trained using the MNIST data. The data has been obtained from <a href="https://www.kaggle.com/c/digit-recognizer/data" style="text-decoration:none;">this</a> link. The simple model has reached accuracy of 98.7% and reaches around 99.5% when rotational and linear translational variances are also considered. Although it is true that the data provided is clean and not very difficult for a model to learn it still can be said how good CNNs work when it comes to pattern observations.</p>
 
   <h3> Identifying Digits: </h3>
    <p style = "font-weight: 400; font-size: 15px;" align="justify"> In this section apart from solving the <a href="https://www.kaggle.com/c/digit-recognizer" style="text-decoration:none;">kaggle challenge</a> above I have extended it to finding digits in live videos or images and classifying them. Here the main objective is - given a frame containing a number, identifying and correctly cropping and resizing it so that it can be provided into the trained classifier model to get the output. So to perform the task the following flow is being used:<br><br>
<center>
    <img src="/images/lhwdc/flowchart.jpg" alt="centered image">
 </center>
    <br>
 <br>
    A sample of how the above images look at each stage of processing:
 <br>
 
  <table width="600" border="1" cellpadding="5">
   <tr>
   <td align="center" valign="center">
   <img src="/images/lhwdc/4/gray.jpg" alt="description here" />
   <br />
   Image after converting to Gray Scale.
   </td>
   
   <td align="center" valign="center">
   <img src="/images/lhwdc/4/blur.jpg" alt="description here" />
   <br />
   Bluring the image.
   </td>
   
   <td align="center" valign="center">
   <img src="/images/lhwdc/4/edge.jpg" alt="description here" />
   <br />
   Applying edge detector on the blurred image.
   </td>

   </tr>
   <tr>
 
   <td align="center" valign="center">
   <img src="/images/lhwdc/4/thresh.jpg" alt="description here" />
   <br />
   Applying a threshold to the previous image.
   </td>

   <td align="center" valign="center">
   <img src="/images/lhwdc/4/dil.jpg" alt="description here" />
   <br />
   Diluting image.
   </td>
   
   <td align="center" valign="center">
   <img src="/images/lhwdc/4/bbox.jpg" alt="description here" />
   <br />
   Final Bounding box.
   </td>

   </tr>
   </table>

  <p style = "font-weight: 400; font-size: 15px;" align="justify">So, once the image is extracted we feed it into the pretrained model, generated using the previous mentioned point, and get the output. As we can see even if we move the live image it still can extract the number by its own. For the ease of demonstration I have made a GUI application that does the mentioned work. Just to see the working I have put the recording of the same at <a href="https://deepayanbardhan.github.io/portfolio/hand-written-digit-classification/" style="text-decoration:none;">this</a> link.</p>
    </p>
 </div>
