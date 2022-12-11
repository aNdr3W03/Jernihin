# Jernihin

Click here to view <a href="https://jernihin.up.railway.app" title="Jernihin" target="_blank"><b>Jernihin</b></a>.

<a href="https://jernihin.up.railway.app" title="Jernihin Homepage" target="_blank">
  <img src="https://user-images.githubusercontent.com/77439245/206903737-15a2b3f3-e885-4909-a8c7-38eeb2edd154.png" alt="Jernihin Homepage">
</a>

<br>

# Table of Content

- [Jernihin](#jernihin)
- [Table of Content](#table-of-content)
- [About Jernihin](#about-jernihin)
  - [Background](#background)
  - [Goal \& Aim](#goal--aim)
  - [Installation \& Deployment](#installation--deployment)
    - [Project Installation to Personal Virtual Environment](#project-installation-to-personal-virtual-environment)
    - [Deploy Machine Learning Model with Flask on Railway](#deploy-machine-learning-model-with-flask-on-railway)
  - [How Jernihin Work - Water Quality Classification](#how-jernihin-work---water-quality-classification)
  - [Plans \& Realization](#plans--realization)
  - [Repository \& Branch](#repository--branch)
  - [Bibliography](#bibliography)
    - [A. Dataset](#a-dataset)
    - [B. Resources](#b-resources)
    - [C. Academic Papers](#c-academic-papers)
    - [D. References](#d-references)
  - [Presentation](#presentation)
  - [Demo Video](#demo-video)
  - [Developers](#developers)

<br>

# About Jernihin

**Jernihin** is a machine learning program on an Indonesian-based website which is currently in the process of being developed by 4 developers from the SIB3 Capstone C22-078 Team in the **Machine Learning and Front-End Web Developer Program by SIB Dicoding X Kampus Merdeka Batch 3**.

<br>

## Background

A natural resource that has great potential for living things and continues to increase every year is water. According to the Data on Sustainable Development Goals (SDGs), Indonesia's water quality index for 2020 is 53.53, an increase from the previous year [[1]](#c-academic-paper-link "Sistem Prediksi Kualitas Air Yang Dapat Dikonsumsi Dengan Menerapkan Algoritma K-Nearest Neighbor"). Water measurements can be seen from chemical variables such as pH value, turbidity, phosphorus, nitrogen, oxygen, and others which play an important role in determining the quality of water. To find out the quality of the water needs to be monitored regularly [[2]](#c-academic-paper-link "Analisis Kualitas Air pada Jalur Distribusi Air Bersih di Gedung Baru Fakultas Ekonomi dan Manajemen Institut Pertanian Bogor").

One of the efforts to assist the water resources management strategy is to create a system that can monitor the quality of water content. Based on the problems above, we decided to build a website application using deep learning methods to predict water quality from several variables. This application is expected to provide another alternative in the management and monitoring of water quality.

<br>

## Goal & Aim

Based on the background described above, the goal and aim of this project are:

- This website aims to help the community as a utility to help decide and determine water quality. This feature is expected to help in better management of water resources. 

- Jernihin has a feature that can help people to identify water quality based on the content in the water which consists of Fecal, Oxygen, pH, Sediment, Temperature, Nitrogen, Phosphorus, and Turbidity. This feature should be able to help its users to map and identify water quality.

<br>

## Installation & Deployment

This step will be explained briefly through two stages, consisting of:

1. Create the Flask framework on the project
2. Hosting process to Railway

---

### Project Installation to Personal Virtual Environment

The steps to create your virtual environment from this project is as follows:

1. Clone this Repository
   ```bash
   git clone https://github.com/aNdr3W03/Jernihin.git
   ```

2. Install Python Virtual Environment
   ```bash
   virtualenv venv
   ```

3. Install All the Requirements Inside "requirements.txt"
   ```bash
   pip install -r requirements.txt
   ```

4. Import Flask App & Run Server
   ```bash
   export FLASK_APP=app.py
   flask run
   ```
   or
   ```bash
   python app.py
   ```

5. Stop the application program or server by `ctrl + c`.

---

### Deploy Machine Learning Model with Flask on Railway

1. <a href="https://railway.app/login" title="Railway Login" target="_blank"><b>Login</b></a> to Railway account with Email or Github Acoount

2. Create <a href="https://railway.app/new" title="Railway New Project" target="_blank"><b>New Project</b></a>

3. Choose **Deploy form GitHub repo**

4. Choose respository project that you want to deploy

<br>

## How Jernihin Work - Water Quality Classification

1. Get user input from the HTML form in the form of Fecal, Oxygen, pH, Sediment, Temperature, Nitrogen, Phosphorus, and Turbidity. These parameters are extracted as replacement values which will be predicted later. The value range is between 0 and 100 for each input.

2. Scale the user input into the NumPy array for inference.

3. Predict the user input using the model that has been made. The model used is the Random Forest Classifier ensemble tree-based learning algorithm. This will return the result of an array of model predictions from all inputs that have been entered.

4. Output predictive labels in the form of obtaining real legible results. Then, this integer value is converted to a result string based on the label that matches the sign. The result of this process is a series of predictive outcomes, such as "Excellent", "Good", "Fair", "Marginal", and "Poor".

5. The final prediction result is returned to the prediction page to be displayed to the user.

<br>

## Plans & Realization

Risk management planning and possible problems that will occur during the work of this project was carried out using SWOT analysis, namely Strengths, Weaknesses, Opportunities, and Threats. This analysis was conducted to map and identify the strengths, weaknesses, opportunities, and threats that might occur during the development of this project.

For the initial document, a Gantt Chart has been made for tracking the beginning of the agreed-to-do list. Making a Gantt Chart done on ProjectLibre for details of the schedule can be seen in the Gantt Chart document on the following Gantt Chart link, or in the image below:

<a href="https://drive.google.com/drive/folders/1MdgNszSIeeMjoXn2jeHOtU7ZDhLj8h68" title="Jernihin Project Gantt Chart" target="_blank">
  <img src="https://user-images.githubusercontent.com/77439245/206624763-e7d47744-7e0c-4411-be4c-d3e6f7de44ff.png" alt="Jernihin Project Gantt Chart" style="width: 100%">
</a>

<a href="https://drive.google.com/drive/folders/1MdgNszSIeeMjoXn2jeHOtU7ZDhLj8h68" title="Jernihin Project Gantt Chart" target="_blank">Jernihin Project Gantt Chart</a>

<br>

## Repository & Branch

This **Jernihin Repository** is divided into **2 branches**:

- **main** (master branch)
  
  The `main` branch is used as an integration branch for front end display development and machine learning model development. The plan is to use the Flask framework to build and integrate websites and machine learning model as a whole website.

- **dev** (development branch)
  
  The `dev` branch is used during the process of determining the initial resources or it can be called an environment where to try different things to be used in the project so that eventually when you have found the appropriate resources, the docs will be moved from dev to main branch.
    
<br>

## Bibliography

### A. Dataset

<a href="https://data.amerigeoss.org" title="AmeriGEOSS Community Platform DataHub" target="_blank">
  <img src="https://user-images.githubusercontent.com/77439245/206162481-5b17dfc2-fc1e-4f0a-a183-8935999becbc.png" alt="AmeriGEOSS Community Platform DataHub" style="width: 250px">
</a>
  
AmeriGEOSS Community Platform DataHub  
<a href="https://data.amerigeoss.org/dataset/wqi-parameter-scores-1994-2013-b0941" title="Water Quality Index Parameter Scores 1994-2013 Dataset" target="_blank">WQI Parameter Scores 1994-2013 Dataset</a>

### B. Resources

In working on this project, several project or project resources are needed resources.

- **Language**
  
  <a href="https://www.w3schools.com/html" title="HTML5" target="_blank">
    <img src="https://img.shields.io/badge/html5-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white" />
  </a> &nbsp;
  <a href="https://www.w3schools.com/css" title="CSS3" target="_blank">
    <img src="https://img.shields.io/badge/css3-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white" />
  </a> &nbsp;
  <a href="https://www.javascript.com" title="JavaScript" target="_blank">
    <img src="https://img.shields.io/badge/javascript-%23F7DF1E.svg?&style=for-the-badge&logo=javascript&logoColor=black" />
  </a> &nbsp;
  <a href="https://www.python.org" title="Python" target="_blank">
    <img src="https://img.shields.io/badge/python-3670A0.svg?style=for-the-badge&logo=python&logoColor=ffdd54" />
  </a> &nbsp;
  
- **Framework**
  
  <a href="https://getbootstrap.com" title="Bootstrap" target="_blank">
    <img src="https://img.shields.io/badge/bootstrap-%237952B3.svg?&style=for-the-badge&logo=bootstrap&logoColor=white" />
  </a> &nbsp;
  <a href="https://flask.palletsprojects.com" title="Flask" target="_blank">
    <img src="https://img.shields.io/badge/flask-%23000000.svg?&style=for-the-badge&logo=flask&logoColor=white" />
  </a> &nbsp;
  
- **Library**
  
  <a href="https://jquery.com" title="jQuery" target="_blank">
    <img src="https://img.shields.io/badge/jquery-%230769AD.svg?&style=for-the-badge&logo=jquery&logoColor=white" />
  </a> &nbsp;
  <a href="https://pandas.pydata.org" title="Pandas" target="_blank">
    <img src="https://img.shields.io/badge/pandas-%23150458.svg?&style=for-the-badge&logo=pandas&logoColor=white" />
  </a> &nbsp;
  <a href="https://numpy.org" title="NumPy" target="_blank">
    <img src="https://img.shields.io/badge/numpy-%23013243.svg?&style=for-the-badge&logo=numpy&logoColor=white" />
  </a> &nbsp;
  <a href="https://scikit-learn.org" title="scikit-learn" target="_blank">
    <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?&style=for-the-badge&logo=scikit-learn&logoColor=3499CD" />
  </a> &nbsp;
  <a href="https://matplotlib.org" title="Matplotlib" target="_blank">
    <img src="https://custom-icon-badges.demolab.com/badge/matplotlib-66baea.svg?style=for-the-badge&logo=matplotlib" />
  </a> &nbsp;
  <a href="https://seaborn.pydata.org" title="Seaborn" target="_blank">
    <img src="https://custom-icon-badges.demolab.com/badge/seaborn-white.svg?style=for-the-badge&logo=seaborn" />
  </a> &nbsp;
  <a href="https://docs.python.org/3/library/pickle.html" title="Pickle" target="_blank">
    <img src="https://img.shields.io/badge/pickle-%23ffffff.svg?style=for-the-badge&logo=pickle&logoColor=black" />
  </a> &nbsp;
  
- **Icons and Images**
  
  <a href="https://fontawesome.com" title="Font Awesome" target="_blank">
    <img src="https://img.shields.io/badge/font%20awesome-%23339AF0.svg?&style=for-the-badge&logo=font%20awesome&logoColor=white" />
  </a> &nbsp;
  <a href="https://unsplash.com" title="Unsplash" target="_blank">
    <img src="https://img.shields.io/badge/unsplash-%23000000.svg?&style=for-the-badge&logo=unsplash&logoColor=white" />
  </a> &nbsp;
  
- **Deployment**
  
  <a href="https://railway.app" title="Railway App" target="_blank">
    <img src="https://custom-icon-badges.demolab.com/badge/railway-white.svg?style=for-the-badge&logo=railway-app" />
  </a> &nbsp;

### C. Academic Papers

- [1] H. Said, N. H. Matondang and H. N. Irmanda, "Sistem Prediksi Kualitas Air Yang Dapat Dikonsumsi Dengan Menerapkan Algoritma K-Nearest Neighbor," *Seminar Nasional Mahasiswa Ilmu Komputer dan Aplikasinya (SENAMIKA)*, vol. 3, no. 1, pp. 158-168, Apr. 2022. Accessed: Oct. 12, 2022. [Online]. Available: <a href="https://conference.upnvj.ac.id/index.php/senamika/article/view/2017" target="_blank">https://conference.upnvj.ac.id/index.php/senamika/article/view/2017</a>
  
- [2] M. H. D. Barang dan S. K. Saptomo, "Analisis Kualitas Air pada Jalur Distribusi Air Bersih di Gedung Baru Fakultas Ekonomi dan Manajemen Institut Pertanian Bogor," *Jurnal Teknik Sipil dan Lingkungan (J-SIL)*, vol. 4, no. 1, pp. 13-24, Apr. 2019. Accessed: Oct. 12, 2022. doi: 10.29244/jsil.4.1.13-24. [Online]. Aivailable: <a href="https://journal.ipb.ac.id/index.php/jsil/article/view/23735" target="_blank">https://journal.ipb.ac.id/index.php/jsil/article/view/23735</a>

### D. References

- [3] Government of Newfoundland and Labrador, "*Drinking Water Quality Index.*" <a href="https://www.gov.nl.ca" target="_blank">gov.nl.ca</a>. <a href="https://www.gov.nl.ca/ecc/waterres/quality/drinkingwater/dwqi" target="_blank">https://www.gov.nl.ca/ecc/waterres/quality/drinkingwater/dwqi</a> (accessed October 12, 2022).

- [4] Nutan, "*Deploy Machine Learning Model with Flask on Heroku.*" <a href="https://medium.com" target="_blank">medium.com</a>. <a href="https://medium.com/@nutanbhogendrasharma/deploy-machine-learning-model-with-flask-on-heroku-cd079b692b1d" target="_blank">https://medium.com/@nutanbhogendrasharma/deploy-machine-learning-model-with-flask-on-heroku-cd079b692b1d</a> (accessed October 12, 2022).

- [5] A. Sridhar, "*How to Deploy Machine Learning Model using Flask (Iris Dataset) | Python.*" <a href="https://youtube.com" target="_blank">youtube.com</a>. <a href="https://youtu.be/2LqrfEzuIMk" target="_blank">https://youtu.be/2LqrfEzuIMk</a> (accessed November 23, 2022).

- [6] K. Naik, "*Deploy Machine Learning Model using Flask.*" <a href="https://youtube.com" target="_blank">youtube.com</a>. <a href="https://youtu.be/UbCWoMf80PY" target="_blank">https://youtu.be/UbCWoMf80PY</a> (accessed November 23, 2022).

<br>

## Presentation

<a href="https://youtu.be/6C62ByQk4Io" title="Jernihin Presentation Video" target="_blank">
  <img src="https://user-images.githubusercontent.com/77439245/206904492-d995616d-9741-4aca-8582-e9a091bd7c6c.png" alt="Jernihin Presentation Video" style="width: 500px">
</a>

<br>

## Demo Video

<a href="https://youtu.be/1wf-pGftGB0" title="Jernihin Demo Video" target="_blank">
  <img src="https://user-images.githubusercontent.com/77439245/206904471-bce8aaaa-91f4-43a4-8030-f4cb558d7e41.png" alt="Jernihin Demo Video" style="width: 500px">
</a>

<br>

## Developers

Merdeka Belajar Kampus Merdeka (MBKM) 2022  
SIB Dicoding Cycle 3  
**C22-078 Capstone Team**  

- **M319X0851** - <a href="https://github.com/aNdr3W03" title="GitHub Andrew Benedictus Jamesie" target="_blank">Andrew Benedictus Jamesie</a>
- **M319Y0854** - <a href="https://github.com/chelizaaa" title="GitHub Cheliza Sriayu Simarsoit" target="_blank">Cheliza Sriayu Simarsoit</a>
- **M248X0512** - <a href="https://github.com/gilangaleyusta" title="GitHub A. Gilang Aleyusta Savada" target="_blank">A. Gilang Aleyusta Savada</a>
- **M182Y0310** - <a href="https://github.com/adstika20" title="GitHub Ades Tikaningsih" target="_blank">Ades Tikaningsih</a>
