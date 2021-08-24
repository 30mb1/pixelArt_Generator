import os


# THIS SHOULD BE SETUP MANUALLY! USED FOR BUILDING UI
# SHOULD BE ORDERED BY LAYER PRIORITY!!!!!
attrs_labels = ['background', 'body', 'shirt', 'scarf', 'head', 'glasses']
LABEL_TO_PATH = {}
LABEL_TO_COUNT = {}
TOTAL = 1

for label in attrs_labels:
    dir = f"source/{label}"
    list_ = os.listdir(dir)
    LABEL_TO_PATH[label] = f'source/{label}/{label}'+'{}.png'
    LABEL_TO_COUNT[label] = len(list_)
    TOTAL *= len(list_)
