import albumentations as A

transform = A.Compose([

    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    A.Resize(250,250),
])


TTA_transform = A.Compose([ 
    A.GaussBlur(p=0.2),
  
])


type_transform = A.Compose([ 
    A.RandomBrightnessContrast(p=0.2),
    A.Normalize(),
])


