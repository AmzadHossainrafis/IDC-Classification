import torch
import numpy as np
import os
from torch.utils.data import Dataset 
from cv2 import imread
import pandas as pd 



class IDCDATALOADER(Dataset):
    '''
    args : data_dir : str : path to the data directory 
           ransform : torchvision.transforms : data augmentation techniques
           config : dict : configuration dictionary
           batch_size : int : batch size           
    return : image : torch.tensor : image tensor

    summary : This class is used to load the IDC dataset. 
            It inherits from the Dataset class of PyTorch.
    
    
    '''
    def __init__(self,data_df_path,transform=None):
        
        
        self.data_df_path= pd.read_csv(data_df_path)
        self.transform = transform
    

    def __len__(self):
        """
            return : int : length of the dataset 
        """
        return len(self.data_df_path)
    
    def __getitem__(self, idx):
        """
            arg : idx : int : index of the image to be loaded 
            return : image : torch.tensor : image tensor 
        
        """
        image = imread(self.data_df_path.iloc[idx,0])
        label = self.data_df_path.iloc[idx,1]
        if self.transform:
            image = self.transform(image=image)['image']
        return image, label
    