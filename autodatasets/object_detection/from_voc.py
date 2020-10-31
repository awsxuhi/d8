# This file is generated from object_detection/from_voc.md automatically through:
#    d2lbook build lib
# Don't edit it directly

from autodatasets.object_detection import Dataset

def make_ml(name):
    camel_case = name.replace('-',' ').title().replace(' ', '')
    url = f'https://arcraftimages.s3-accelerate.amazonaws.com/Datasets/{camel_case}/{camel_case}PascalVOC.zip'
    return Dataset.from_voc(url, 'images', 'annotations')

names = ['sheep', 'paper-prototype', 'raccoon', 'boggle-boards', 'plant-doc', 
         'hard-hat-workers', 'pistol', 'cars-and-traffic-signs', 'tomato', 
         'dice', 'potholes', 'ships', 'mask', 'chess', 'mobile-phones', 
         'glasses', 'road-signs', 'fruits', 'bikes', 'headphones', 'fish',
         'drone', 'car-license-plates', 'pets', 'faces', 'helmets', 'clothing',
         'hands', 'soccer-ball'
        ]

for name in names:
    Dataset.add(name, make_ml, [name])

import autodatasets as ad
from autodatasets.object_detection import dataset 
import pandas as pd 

@Dataset.add
def stanford_dogs():
    reader = ad.create_reader(ad.download('kaggle:jessicali9530/stanford-dogs-dataset'))
    images = reader.list_images()
    entries = []
    for img in images:
        xml_fp = 'annotations/Annotation/'+img.parent.name+'/'+img.stem
        for label in dataset.parse_voc_annotation(reader.open(xml_fp)):
            label.filepath = str(img)
            entries.append(label)
    return Dataset(reader, pd.DataFrame(entries))


