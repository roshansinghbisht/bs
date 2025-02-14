import os
from zipfile import ZipFile
import glob
import handle_zero_id as z
import create_masked_images as cmi


def make_dir(dirpath):
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)


def unzip_data_and_perform_data_aug():
        """
        """
        # train_dir = os.path.join(datadownloadDir, "train")
        # test_dir = os.path.join(datadownloadDir, "test")
        # train_mask_dir = os.path.join(datadownloadDir, "train_mask")
        # test_mask_dir = os.path.join(datadownloadDir, "test_mask")
        # make_dir(train_dir)
        # make_dir(test_dir)
        # make_dir(train_mask_dir)
        # make_dir(test_mask_dir)
        # #
        # train_set_dir = os.path.join(train_dir, "train_set")
        # train_extracted_dir = os.path.join(train_dir, "train_set_extract")
        # train_mask_extracted_dir = os.path.join(train_mask_dir, "train_set_extract")
        # test_set_dir = os.path.join(test_dir, "test_set")
        # test_extracted_dir = os.path.join(test_dir, "test_set_extract")
        # test_mask_extracted_dir = os.path.join(test_mask_dir, "test_set_extract")
        # make_dir(train_extracted_dir)
        # make_dir(test_extracted_dir)

        test_set_dir = "/Users/roshanbisht/Documents/code/bs-ocr/data/test_OCR"
        test_extracted_dir = "/Users/roshanbisht/Documents/code/bs-ocr/data/test_OCR/test_set_extract"
        test_mask_extracted_dir = "/Users/roshanbisht/Documents/code/bs-ocr/data/test_OCR/test_mask"


        for item in os.listdir(test_set_dir):
            dirname = os.path.join(test_extracted_dir, item.split(".")[0])
            with ZipFile(os.path.join(test_set_dir, item)) as zip_obj:
                zip_obj.extractall(dirname)
            
            # filename = glob.glob(dirname + "/**/*.json")[0]
            # hzi = z.handle_zero_id_in_coco_json(filename)
            # hzi.main()
            # in_between_path = filename.rpartition('/')[0].split('test_set_extract/')[-1]
            # mask_images_path = os.path.join(test_mask_extracted_dir, in_between_path, "images/")
            # make_dir(mask_images_path)
            # mask_obj = cmi.create_masked_images(filename)
            # mask_obj.main(mask_images_path)
            break


        # for item in os.listdir(train_set_dir):
        #     dirname = os.path.join(train_extracted_dir, item.split(".")[0])
        #     with ZipFile(os.path.join(train_set_dir, item)) as zip_obj:
        #         zip_obj.extractall(dirname)

        #     filename = glob.glob(dirname + "/**/*.json")[0]
        #     hzi = z.handle_zero_id_in_coco_json(filename)   
        #     hzi.main()
        #     in_between_path = filename.rpartition('/')[0].split('train_set_extract/')[-1]
        #     mask_images_path = os.path.join(train_mask_extracted_dir, in_between_path, "images/")
        #     make_dir(mask_images_path)
        #     mask_obj = cmi.create_masked_images(filename)
        #     mask_obj.main(mask_images_path)



unzip_data_and_perform_data_aug()