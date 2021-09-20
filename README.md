# Covid Detection Using Deep Learning
<h2>Overview</h2>
Covid-19 is one of the biggest challenges mankind is facing these days. One of the important factors, which can prove to be revolutionary in our fight against the ongoing pandemic is the fast and reliable ways of testing. Invasive methods of testing is a cumbersome process and might prove to be road-block in our road to fast testing. Moreover, there is a chance of spread of infection, while using the invasive methods, due to highly contagious nature of the disease. <br> <br>
I propose a method of fast and non-invasive testing of COVID-19 in which cutting-edge technology (Artificial Intelligence) is used to classify, whether the X-Ray image of the person is Covid-19 positive or not. <br> <br>
<b>The project is deployed on Heroku: <a href="https://covid-classifier-xrays.herokuapp.com/">https://covid-classifier-xrays.herokuapp.com/</a></b>
<hr>
<h2>Dataset and Libraries</h2>
<p>
  <b>Dataset :</b> There is a combination of two-datasets: Covid-19 Positive and Normal <br>
Normal Dataset: <b><a href="https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia">https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia</a></b><br>
COVID-19 Positive Dataset: <b><a href="https://github.com/ieee8023/covid-chestxray-dataset">https://github.com/ieee8023/covid-chestxray-dataset</a></b><br> <br>
<b>Libraries : </b>Python , Numpy , Pandas, Sklearn , Node.js , Tensorflow.<br>
<b>Tools and Technologies : </b>PyCharm , Jupyter Notebook, Google Colab, Heroku.<br>
</p>
<hr>
<h2>Methodology of Development</h2>
<p>
In this project, I have developed a Convolutional Based Neural Network Deep Learning Model to classify whether the particular X-Ray image is of a COVID-19 Positive Patient or not. The steps used in development of the machine learning model are listed below: <br> <br>
  
  <b> 1. Dataset Preparation </b> <br> <br> The dataset for the deep-learning model is developed, by combining the datasets for COVID-19 Positive Patients and Normal Patients. About 150 images are used for both of the classes. The dataset available on Github consisted of images for different respiratory diseases. I have picked only the those, who are related with COVID-19. <br> <br>
  
  <b> 2. Data-Preprocessing and Image Augmentation </b> <br> <br> The prepared dataset is then preprocessed using different preprocessing techniques. Data Augmentation techniques like resizing, shearing and zooming are used, for increasing the data for deep learning models (Data Hungry :p) . The images are not horizontally flipped, because the X-Ray images might differ, when horizontally flipped, because it is necessary that if an anamoly is present on the right side, then the same anamoly on left side will yield the same results. <br> <br>
  ![image](https://user-images.githubusercontent.com/48025630/134042565-0891001e-df66-4ed8-8fc5-21697c264273.png)

  
  <b> 3. Model Architecture and Training </b> <br> <br> Then, the architecture of the Convolutional Neural Network is developed. The dataset is trained on different architectures, to optimize the results. Apart from accuracy, a major focus is put on the Recall of the Classification Model, because in Medical Image Diagnosis, predicting a patient as False Positive, can prove to be fatal. <br> The optimizer used for training is <b> Adam Optimizer </b>, while the loss is <b> Binary Cross-Entropy Loss </b>. The activation functions for the hidden layers is <b> ReLU (Rectified Linear Unit) </b>, while for the final layer, it is <b> Sigmoid </b> <br> <br>
  ![image](https://user-images.githubusercontent.com/48025630/134043789-5345da42-22b1-4afb-a0e5-784f005d7d8a.png)

  
  <b> 4. Model Deployment </b> <br> <br> The model is saved in the form of "H5 File" and is deployed on the cloud, using Heroku Cloud Deployment, with the help of Flask Library of Python. <br> <br>
 
</p>
 <hr>
 <h2>Diagrammatic Representation of Working</h2>
 <img src="https://github.com/anshuljain2607/COVID-Detection-using-Deep-Learning/blob/master/Screenshots/Working.PNG">
<hr>
<h2>Screenshots of the Web-Application</h2>
<b><p>Initial Page/Landing Page</p></b>
<img src="https://github.com/anshuljain2607/COVID-Detection-using-Deep-Learning/blob/master/Screenshots/1.PNG">
<b><p>Uploading the X-Ray Image</p></b>
<img src="https://github.com/anshuljain2607/COVID-Detection-using-Deep-Learning/blob/master/Screenshots/2.PNG">
<b><p>Printing the Prediction.</p></b>
<img src="https://github.com/anshuljain2607/COVID-Detection-using-Deep-Learning/blob/master/Screenshots/3.PNG">
<hr>
<h2>Running the Project</h2>
<p><b>1. Accesing the website online </b></p>
  <p> To access the website and check its working you can visit this link <a href="https://covid-classifier-xrays.herokuapp.com/">https://covid-classifier-xrays.herokuapp.com/</a> <br>
 <p><b>2. Copying to local repository </b></p>
  <p> In your terminal run the following commands : <br><br>
     <b>
     git clone https://github.com/anshuljain2607/COVID-Detection-using-Deep-Learning.git<br>
     cd COVID-Detection-using-Deep-Learning<br>
     python app.py<br>
     Open https://localhost:3000 <br>
     </b>
  </p>
 <hr>
 <h2>Contributors</h2>
 <p><a href="https://github.com/anshuljain2607">Anshul Jain</a></p>
 <hr>
