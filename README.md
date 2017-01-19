# annotation_scripts
Scripts that were used to annotate the dataset.

 - *annotate.py* <offset> <classname> is how we use the script. The offset needs to be entered everytime we are done with a class. It also writes class specific information in the *ImageSets/Main* folder.
 - *check_anno.py* will check the traverse the *Annotations* and *JPEGImages* directory to check for missing files, the order is very important for us.
 - *correct_xml.py* will check for the area of the bounding box and also if xmax is truly greater than xmin and similarly for the y coordinate.
  - *annotate_mod.py* is similar to the annotate.py, only difference is that it ignores the class specific information. This should only be used if the *check_anno.py* reports errors.
  - *shuffle.py* will shuffle the class specific information according the a file train.txt which has a numbered list in sorted order. What it does effectively is to shuffle the main list and then based on this list, it modifies the content of the other lists that have the class specific information, i.e. if the class is present or not in that particular file.

# training steps for py-faster-rcnn

- First download and build *py-faster-rcnn*.
- Our dataset was already prepared in the format that pascal_voc expects. All we have to do is create a symlink in the *py-faster-rcnn/data* directory named *VOCdevkit2007* to our data directory.
- Then clear the *py-faster-rcnn/data/cache* directory since it stores the roidb in that directory for reuse. It causes problems when a new dataset arrives.
- Edit the *py-faster-rcnn/lib/datasets/pascal_voc.py* file and change the self.classes_ list to contain our own classes.
- Edit the *py-faster-rcnn/models/pascal_voc/{VGG16 | ZF}/faster_rcnn_end2end/train.txt* and change the *num_classes* and *num_classes* parameter to your __number of classes__ + __background__ and the *num_output* parameter to (4 * *num_classes*) in bbox_pred layer.
- Run *py-faster-rcnn/experiments/scripts/faster_rcnn_end2end 0 VGG16 pascal_voc* to start training.
