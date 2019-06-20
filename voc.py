# VOC dataset utility functions
import numpy as np


VOC_CLASSES_LIST = [
    'aeroplane',
    'bicycle',
    'bird',
    'boat',
    'bottle',
    'bus',
    'car',
    'cat',
    'chair',
    'cow',
    'diningtable',
    'dog',
    'horse',
    'motorbike',
    'person',
    'pottedplant',
    'sheep',
    'sofa',
    'train',
    'tvmonitor'
]

VOC_CLASSES_SET = set(VOC_CLASSES_LIST)

VOC_CLASS_ID = {
    cls_name: idx for idx, cls_name in enumerate(VOC_CLASSES_LIST)
}

# Random RGB colors for each class (useful for drawing bounding boxes)
VOC_COLORS = \
    np.random.uniform(0, 255, size=(len(VOC_CLASSES_LIST), 3)).astype(np.uint8)


COCO_CLASSES_LIST = [
    'unlabeled',
    'person',
    'bicycle',
    'car',
    'motorcycle',
    'airplane',
    'bus',
    'train',
    'truck',
    'boat',
    'traffic light',
    'fire hydrant',
    'street sign',
    'stop sign',
    'parking meter',
    'bench',
    'bird',
    'cat',
    'dog',
    'horse',
    'sheep',
    'cow',
    'elephant',
    'bear',
    'zebra',
    'giraffe',
    'hat',
    'backpack',
    'umbrella',
    'shoe',
    'eye glasses',
    'handbag',
    'tie',
    'suitcase',
    'frisbee',
    'skis',
    'snowboard',
    'sports ball',
    'kite',
    'baseball bat',
    'baseball glove',
    'skateboard',
    'surfboard',
    'tennis racket',
    'bottle',
    'plate',
    'wine glass',
    'cup',
    'fork',
    'knife',
    'spoon',
    'bowl',
    'banana',
    'apple',
    'sandwich',
    'orange',
    'broccoli',
    'carrot',
    'hot dog',
    'pizza',
    'donut',
    'cake',
    'chair',
    'couch',
    'potted plant',
    'bed',
    'mirror',
    'dining table',
    'window',
    'desk',
    'toilet',
    'door',
    'tv',
    'laptop',
    'mouse',
    'remote',
    'keyboard',
    'cell phone',
    'microwave',
    'oven',
    'toaster',
    'sink',
    'refrigerator',
    'blender',
    'book',
    'clock',
    'vase',
    'scissors',
    'teddy bear',
    'hair drier',
    'toothbrush',
]

COCO_CLASSES_SET = set(COCO_CLASSES_LIST)

COCO_CLASS_ID = {
    cls_name: idx for idx, cls_name in enumerate(COCO_CLASSES_LIST)
}

# Random RGB colors for each class (useful for drawing bounding boxes)
COCO_COLORS = \
    np.random.uniform(0, 255, size=(len(COCO_CLASSES_LIST), 3)).astype(np.uint8)


def convert_coco_to_voc(label):
    """Converts COCO class name to VOC class name, if possible.

    COCO classes are a superset of VOC classes, but
    some classes have different names (e.g. airplane
    in COCO is aeroplane in VOC). This function gets
    COCO label and converts it to VOC label,
    if conversion is needed.

    Args:
        label (str): COCO label
    Returns:
        str: VOC label corresponding to given label if such exists,
            otherwise returns original label
    """
    COCO_VOC_DICT = {
        'airplane': 'aeroplane',
        'motorcycle': 'motorbike',
        'dining table': 'diningtable',
        'potted plant': 'pottedplant',
        'couch': 'sofa',
        'tv': 'tvmonitor'
    }
    if label in COCO_VOC_DICT:
        return COCO_VOC_DICT[label]
    else:
        return label

def coco_label_to_voc_label(label):
    """Returns VOC label corresponding to given COCO label.

    COCO classes are superset of VOC classes, this function
    returns label corresponding to given COCO class label
    or None if such label doesn't exist.

    Args:
        label (str): COCO class label
    Returns:
        str: VOC label corresponding to given label or None
    """
    label = convert_coco_to_voc(label)
    if label in VOC_CLASSES_SET:
        return label
    else:
        return None

def is_voc_label(label):
    """Returns boolean which tells if given label is VOC label.

    Args:
        label (str): object label
    Returns:
        bool: is given label a VOC class label
    """
    return label in VOC_CLASSES_SET

def get_voc_label_color(label):
    """Returns color corresponding to given VOC label, or None.

    Args:
        label (str): object label
    Returns:
        np.array: RGB color described in 3-element np.array
    """
    if not is_voc_label(label):
        return None
    else:
        return VOC_COLORS[VOC_CLASS_ID[label]]
