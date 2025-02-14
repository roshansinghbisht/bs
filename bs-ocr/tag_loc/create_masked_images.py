from pycocotools.coco import COCO
import json
import re
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2


class create_masked_images():
    """Renaming image file name, and filenames in coco annotation file
    """
    def __init__(self, annotation_file_path):
        self.annotation_file_path = annotation_file_path
        # Create a COCO file object
        self.coco_annotation = COCO(annotation_file=self.annotation_file_path)
        # Get image ids from the coco object 
        self.img_ids = self.coco_annotation.getImgIds()
        self.ann_ids = self.coco_annotation.getAnnIds(self.img_ids)
        self.anns = self.coco_annotation.loadAnns(self.ann_ids)


    def get_masked_images(self, masked_images_path):
        for a in [1,2,3]:
            print(a)
        for i in range(len(self.img_ids)):
            img_info = self.coco_annotation.loadImgs(i)[0]
            image_full_name = img_info["file_name"]
            mask = np.zeros((img_info['height'], img_info['width']))
            ann_tag = [ann for ann in self.anns if ann['segmentation'] and ann['image_id']==i][0]
            mask = np.maximum(self.coco_annotation.annToMask(ann_tag), mask)
            print(mask.shape)
            print(np.unique(mask))
            # image_name = image_full_name.split('.')
            # updated_name = image_name[0]+"_masked.jpeg"
            cv2.imwrite(masked_images_path+image_full_name, mask)
            #plt.imsave(masked_images_path+image_full_name, mask)

    
    # def image_blending(self, masked_images_path):
    #     # Create a list containing the current image file names
    #     source_images_path = "tag_localization/images/"
    #     blended_images_path = "tag_localization/blended_images/"

    #     for i in range(len(self.img_ids)):
    #         img_info = self.coco_annotation.loadImgs(i)[0]
    #         image_full_name = img_info["file_name"]
    #         # image_name = image_full_name.split('.')
    #         # masked_image_name = image_name[0]+"_masked."+image_name[1]
    #         src1 = cv2.imread(source_images_path+image_full_name)
    #         src2 = cv2.imread(masked_images_path+image_full_name)
    #         dst = cv2.addWeighted(src1, 0.6, src2, 0.4, 0)
    #         cv2.imwrite(blended_images_path+image_full_name, dst)


    def main(self, masked_images_path):
        self.get_masked_images(masked_images_path)
        # self.image_blending(masked_images_path)


if __name__ == "__main__":
    ann_file_path = "tag_localization/result.json"
    masked_images_path = "tag_localization/masked_images/"
    if not(os.path.isdir("tag_localization/masked_images")):
        os.mkdir("tag_localization/masked_images")
    vaf = create_masked_images(ann_file_path)
    vaf.main(masked_images_path)