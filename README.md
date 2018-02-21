# DESCRIPTION #

This repository provides ROS package to merge two tracking systems, Vicon and Optitrack, in the MIT Building 31's high bay.

### SETUP ###

* Install prerequisites
```
sudo pip install pyquaternion
```

### DATA ###

Please download data and put it `data/` folder.
Data can be found at: `https://drive.google.com/drive/folders/1k5D_k6xLRdH1TWRTjlZ8tqHJ-GOyM9Zb?usp=sharing`.

### RESULT ###
Transformation between Vicon to Opti (based on 3 data points):
```
Position (x, y, z): 12.0174229, 1.11216997, -0.0175561
Quaternion (qx, qy, qz, qw): -0.00083867, 0.00084894, 0.7387037, 0.67402662
```

Further optimized transformation between Vicon to Opti (based on trajectory):
```
Position (x, y, z): 
Quaternion (qx, qy, qz, qw): 
```

### CONTRIBUTION GUIDELINES ###

* Create a new branch if you want to add a new feature to the code base:
```
git checkout -b <branch_name>
```
* Once the feature is complete, create a pull request for a senior student to review your work
```
git add <list files you want to commit>
git commit -m "<commit description>"
git push -u origin <branch_name>
```

### CONTACT ###

* Dong-Ki Kim (dkkim93@mit.edu)
* Jesus Tordesillas (jtorde@mit.edu)
* Shayegan Omidshafiei (shayegan@mit.edu)
