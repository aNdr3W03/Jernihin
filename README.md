<a id="1"></a>

# Jernihin Demo Link
#### [**Click here to view Jernihin**](https://https://jernihin.up.railway.app//)

<br>
<a id="0"></a>

# Table of Content
0. ##### [Table of Content](#0)
1. ##### [Jernihin Demo Link](#1)
2. ##### [About Jernihin](#2)
	1. ###### [Background](#21)
	2. ###### [Goal & Aim](#22)
	3. ###### [How to Install & Deploy to Railways](#23)
		1. [Installation of the Project to Personal Virtual Environment](#231)
		2. [Deploy Machine Learning Model with Flask on Railway](#232)
	4. ###### [Jernihin Work - Water Quality Classification](#24)
	5. ###### [Plans & Realization](#25)
	6. ###### [Repository & Branch](#26)
	7. ###### [Bibliography](#27)
	8. ###### [Developers](#28)


<br>
<a id="2"></a>

# About Jernihin

**Jernihin** is a machine learning program on an Indonesian-based website which is currently in the process of being developed by 4 developers from the SIB3 Capstone C22-078 Team  in the **Machine Learning and Front-End Web Developer Program by SIB Dicoding X Kampus Merdeka Batch 3**.

<br>
<a id="21"></a>

## Background

A natural resource that has great potential for living things and continues to increase every year is water. According to the Data on Sustainable Development Goals (SDGs), Indonesia's water quality index for 2020 is 53.53, an increase from the previous year. Water measurements can be seen from chemical variables such as pH value, turbidity, phosphorus, nitrogen, oxygen, and others which play an important role in determining the quality of water. To find out the quality of the water needs to be monitored regularly.

One of the efforts to assist the water resources management strategy is to create a system that can monitor the quality of water content. Based on the problems above, we decided to build a website application using deep learning methods to predict water quality from several variables. This application is expected to provide another alternative in the management and monitoring of water quality.

<br>
<a id="22"></a>

## Goal & Aim

- This website aims to help the community as a utility to help decide and determine water quality. This feature is expected to help in better management of water resources. 

- Jernihin has a feature that can help people to identify water quality based on the content in the water which consists of Fecal, Oxygen, pH, Sediment, Temperature, Nitrogen, Phosphorus, and Turbidity. This feature should be able to help its users to map and identify water quality

<br>
<a id="23"></a>

## How to Install & Deploy to Railway

This step will be explained briefly through two stages, consisting of:
1. Create the Flask framework
2. Hosting process to Railway

---

<br>
<a id="231"></a>

### Installation of the Project to Personal Virtual Environment

The steps to create your virtual environment from this project is as follows:

1. Clone this repository

```
git clone https://github.com/aNdr3W03/Jernihin.git
```

2. Install Python Virtual Environment

```
virtualenv env
```

3. Install All the Requirements Inside "requirements.txt"

```
pip install -r requirements.txt
```

4. Import Flask App & Run Server

```
export FLASK_APP=app.py
flask run
```

5. Stop the application program or *server* by `ctrl + c`.

<br>
<a id="232"></a>

---

### Deploy Machine Learning Model with Flask on Railways

1. Login account in Railway with Email or Github Acoount: https://railway.app/login

2. Create New Project: https://railway.app/new

3. Choose deploy form GitHub repo

4. Choose respository project that you want to deploy

---

**Credits & Tutorial:**

- [How to Deploy Machine Learning Model using Flask (Iris Dataset) | Python](https://youtu.be/2LqrfEzuIMk)

- [Deploy Machine Learning Model using Flask](https://youtu.be/UbCWoMf80PY)

<br>
<a id="24"></a>

## Jernihin Work - Water Quality Classification

1. Get user input from the HTML form in the form of Fecal, Oxygen, pH, Sediment, Temperature, Nitrogen, Phosphorus, and Turbidity. These parameters are extracted as replacement values ​​which will be predicted later. The value range is between 0 and 100 for each input.

2. Scale the user input into the NumPy array for inference.

3. Predict user input using the model that has been made. The method used is RandomForestClassify. This function returns an array of model beliefs from all inputs that have been entered.

4. Output predictive labels in the form of obtaining real legible results. Then, this integer value is converted to a result string based on the label that matches the sign. The result of this process is a series of predictive outcomes, such as "Excellent", "Good", "Fair", "Marginal", and "Poor".

5. The final prediction result is returned to the display to be displayed to the user.

<br>
<a id="25"></a>

## Plans & Realization

Risk management planning and possible problems that will occur during work on this project was carried out using SWOT analysis, namely Strength, Weaknesses, Opportunities, and Threats. This analysis is carried out to carry out mapping and identification of strengths, weaknesses, opportunities, and threats that may occur when development of this project.

For the initial document, a Gantt Chart has been made for tracking the beginning of the agreed-to-do list. Making Gantt Chart done on ProjectLibre for details of the schedule can be seen in the Gantt Chart document on the following Gantt Chart link, or in the image below:

https://drive.google.com/drive/folders/1MdgNszSIeeMjoXn2jeHOtU7ZDhLj8h68


<br>
<a id="26"></a>

## Repository & Branch

This **Jernihin Repository is divided** into **2 branches**:

- **main** (master)

    The main branch is used as an integration branch for front end display development and machine learning model development. The plan is to use the Flask framework to build and integrate websites and machine learning models as a single website.

- **dev** (test site)

    The dev branch is used during the process of determining the initial resources or it can be called an environment where to try different things to be used in the project so that eventually when you have found the appropriate resources, the docs will be moved from dev to main branch.
    
<br>
<a id="27"></a>

## Bibliography

### A. Dataset Links:

 <a href="https://data.amerigeoss.org" title="AmeriGEOSS Community Platform DataHub" target="_blank">
    <img src="https://user-images.githubusercontent.com/77439245/206162481-5b17dfc2-fc1e-4f0a-a183-8935999becbc.png" alt="AmeriGEOSS Community Platform DataHub" style="width: 250px">
  </a>
  
  AmeriGEOSS Community Platform DataHub  
  <a href="https://data.amerigeoss.org/dataset/wqi-parameter-scores-1994-2013-b0941" title="Water Quality Index Parameter Scores 1994-2013 Dataset" target="_blank">WQI Parameter Scores 1994-2013 Dataset</a>


### B. Resources:
In working on this project, several project or project resources are needed resources.

- Programming Language
  
  <a href="https://www.w3schools.com/html" title="HTML5" target=_blank>
    <img src="https://img.shields.io/badge/html5-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white" />
  </a> &nbsp;
  <a href="https://www.w3schools.com/css" title="CSS3" target=_blank>
    <img src="https://img.shields.io/badge/css3-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white" />
  </a> &nbsp;
  <a href="https://www.javascript.com" title="JavaScript" target=_blank>
    <img src="https://img.shields.io/badge/javascript-%23F7DF1E.svg?&style=for-the-badge&logo=javascript&logoColor=black" />
  </a> &nbsp;
  <a href="https://www.python.org" title="Python" target=_blank>
    <img src="https://img.shields.io/badge/python-3670A0.svg?style=for-the-badge&logo=python&logoColor=ffdd54" />
  </a> &nbsp;
  
- Framework
  
  <a href="https://getbootstrap.com" title="Bootstrap" target=_blank>
    <img src="https://img.shields.io/badge/bootstrap-%237952B3.svg?&style=for-the-badge&logo=bootstrap&logoColor=white" />
  </a> &nbsp;
  <a href="https://flask.palletsprojects.com" title="Flask" target=_blank>
    <img src="https://img.shields.io/badge/flask-%23000000.svg?&style=for-the-badge&logo=flask&logoColor=white" />
  </a> &nbsp;
  
- Library
  
  <a href="https://jquery.com" title="jQuery" target=_blank>
    <img src="https://img.shields.io/badge/jquery-%230769AD.svg?&style=for-the-badge&logo=jquery&logoColor=white" />
  </a> &nbsp;
  <a href="https://pandas.pydata.org" title="Pandas" target=_blank>
    <img src="https://img.shields.io/badge/pandas-%23150458.svg?&style=for-the-badge&logo=pandas&logoColor=white" />
  </a> &nbsp;
  <a href="https://numpy.org" title="NumPy" target=_blank>
    <img src="https://img.shields.io/badge/numpy-%23013243.svg?&style=for-the-badge&logo=numpy&logoColor=white" />
  </a> &nbsp;
  <a href="https://scikit-learn.org" title="scikit-learn" target=_blank>
    <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?&style=for-the-badge&logo=scikit-learn&logoColor=3499CD" />
  </a> &nbsp;
  <a href="https://matplotlib.org" title="Matplotlib" target=_blank>
    <img src="https://custom-icon-badges.demolab.com/badge/matplotlib-66baea.svg?style=for-the-badge&logo=matplotlib" />
  </a> &nbsp;
  <a href="https://seaborn.pydata.org" title="Seaborn" target=_blank>
    <img src="https://custom-icon-badges.demolab.com/badge/seaborn-white.svg?style=for-the-badge&logo=seaborn" />
  </a> &nbsp;
  <a href="https://docs.python.org/3/library/pickle.html" title="Pickle" target=_blank>
    <img src="https://img.shields.io/badge/pickle-%23ffffff.svg?style=for-the-badge&logo=pickle&logoColor=black" />
  </a> &nbsp;
  
- Icons and Images
  
  <a href="https://fontawesome.com" title="Font Awesome" target=_blank>
    <img src="https://img.shields.io/badge/font%20awesome-%23339AF0.svg?&style=for-the-badge&logo=font%20awesome&logoColor=white" />
  </a> &nbsp;
  
- Deployment
  
  <a href="https://railway.app" title="Railway App" target=_blank>
    <img src="https://custom-icon-badges.demolab.com/badge/railway-white.svg?style=for-the-badge&logo=railway-app" />
  </a> &nbsp;

### C. Academic Paper Link:

- [1] H. Said, N. H. Matondang dan H. N. Irmanda, "Sistem Prediksi Kualitas Air Yang Dapat Dikonsumsi Dengan Menerapkan Algoritma K-Nearest Neighbor," *Seminar Nasional Mahasiswa Ilmu Komputer dan Aplikasinya (SENAMIKA)*, vol. 3, no. 1, pp. 158-168, Apr. 2022. Accsess: 12 Okt. 2022. [Online]. Available at : <a href="https://conference.upnvj.ac.id/index.php/senamika/article/view/2017" target=_blank>https://conference.upnvj.ac.id/index.php/senamika/article/view/2017</a>
  
- [2] M. H. D. Barang dan S. K. Saptomo, "Analisis Kualitas Air pada Jalur Distribusi Air Bersih di Gedung Baru Fakultas Ekonomi dan Manajemen Institut Pertanian Bogor," *Jurnal Teknik Sipil dan Lingkungan (J-SIL)*, vol. 4, no. 1, pp. 13-24, Apr. 2019. Accsess: 12 Okt. 2022. doi: 10.29244/jsil.4.1.13-24. [Online]. Aivailable at: <a href="https://journal.ipb.ac.id/index.php/jsil/article/view/23735" target=_blank>https://journal.ipb.ac.id/index.php/jsil/article/view/23735</a>

<br>
<a id="28"></a>

## Developers

Merdeka Belajar Kampus Merdeka (MSIB) 2022  
SIB Dicoding Cycle 3  
**C22-078 Capstone Team**  

- **M319X0851** - <a href="https://github.com/aNdr3W03" title="GitHub Andrew Benedictus Jamesie" target=_blank>Andrew Benedictus Jamesie</a>
- **M319Y0854** - <a href="https://github.com/chelizaaa" title="GitHub Cheliza Sriayu Simarsoit" target=_blank>Cheliza Sriayu Simarsoit</a>
- **M248X0512** - <a href="https://github.com/gilangaleyusta" title="GitHub A. Gilang Aleyusta Savada" target=_blank>A. Gilang Aleyusta Savada</a>
- **M182Y0310** - <a href="https://github.com/adstika20" title="GitHub Ades Tikaningsih" target=_blank>Ades Tikaningsih</a>



