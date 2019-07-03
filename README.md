# TuSimple Lane Challenge Class Labels

This repository contains the class labels for the lane boundaries of the TuSimple lane detection dataset. You can download the dataset from https://github.com/TuSimple/tusimple-benchmark/issues/3.

## Classes

Each lane boundary in the dataset is annotated using 7 different classes. Lanes that cannot be uniquely identified are annotated as `Unknown`. A hierarchical representation of the classes is shown below. Even if the `Double-dashed-continuous` class has been considered during the annotation process for completeness, there are no examples in the dataset of that class. The names of the class ids are in `class_mapping.txt`.

![hierarchy](https://user-images.githubusercontent.com/10325202/60464863-fcd9ea80-9c4f-11e9-8f92-a7158bc10582.png)

## Installation

First of all, download the dataset and extract it. Then, move the files inside the `data` folder inside the resulting folder.

```mv data/* path/to/dataset/train_set```

You can obtain a .json file with an additional `class` field with the `converter.py` script. Launch it with:

```python converter.py --root /path/to/dataset```

It is also possible to visualize the annotations with the `visualizer.py` script. Launch with:

```python visualizer.py --root /path/to/dataset --labels labels_json_file.json```

## Citation

Coming soon.
