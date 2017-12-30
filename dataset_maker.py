import os
import cv2

src_dir = "I:/Pictures/GalaxyS6"
dist_dir = "./dist"

class_dir_list = ["keyaki", "nogi", "sphere", "other"]

if __name__ == "__main__":
    # 画像ファイル分類（フォルダ分け）、ラベル付け（クラス、顔全身位置）
    files = os.listdir(src_dir)
    for file in files:
        print(file)
        path = os.path.join(src_dir, file)

        if os.path.isfile(path):
            pic = cv2.imread(path)
            if pic is None:
                continue
            cv2.imshow("pic", pic)

            key = cv2.waitKey(0)

    print(len(files))
