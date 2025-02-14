import json


class handle_zero_id_in_coco_json():
    """
    """
    def __init__(self, annotation_file_path):
        self.annotation_file_path = annotation_file_path
    

    def update_coco_file(self):
        """
        """
        with open(self.annotation_file_path, "r") as jsonFile:
            data = json.load(jsonFile)

        new_categories = []
        for categories in data['categories']:
                if categories['id'] == 0:
                    categories['id'] = 37
                new_categories.append(categories)
        data['categories'] = new_categories

        new_annotations_data = []
        for anno_info in data['annotations']:
            if anno_info['category_id'] == 0:
                anno_info['category_id'] = 37
            new_annotations_data.append(anno_info)

        data['annotations'] = new_annotations_data

        with open(self.annotation_file_path, "w") as jsonFile:
            json.dump(data, jsonFile)


    def main(self):
        self.update_coco_file()


if __name__ == "__main__":
    ann_file_path = "remove_unwanted_images/result.json"
    vaf = handle_zero_id_in_coco_json(ann_file_path)
    vaf.main()