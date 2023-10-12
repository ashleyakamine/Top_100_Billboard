#  Top 100 Billboard
## About the dataset
The data this week comes from Data.World by way of Sean Miller, Billboard.com and Spotify.

Billboard Top 100 - Wikipedia

The Billboard Hot 100 is the music industry standard record chart in the United States for songs, published weekly by Billboard magazine. Chart rankings are based on sales (physical and digital), radio play, and online streaming in the United States.

Found on Kaggle: https://www.kaggle.com/datasets/sujaykapadnis/top-100-billboard

## Getting Started
### Prerequisites
Before you can clone or pull this repository, please ensure that you have Git LFS (Large File Storage) installed on your system. Git LFS is essential for handling large files efficiently.

If you don't have Git LFS installed, you can download and install it from [https://git-lfs.github.com/](https://git-lfs.github.com/).

## Extra pont 
we create a dictionary performer_counts to store the count of each performer. We then iterate through the billboard data, extract the performer's name from each entry, and update the count in the dictionary. Finally, we use the max function to find the performer with the highest count, which represents the most-listened performer. 

We also created the calculate_correlations method to calculate the correlation coefficient between any two given columns. It takes in the dataframe, and a list of column tuples (if you would like to calculate many correlation coefficients at once). It will output a dictionary with a the two columns mapped to their corresponding correlation coeffiencent.
