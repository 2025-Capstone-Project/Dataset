from glob import glob
import os
import shutil

dataset = "C:/Users/82102/OneDrive/사진/바탕 화면/zip/"

img_list_co = glob(dataset + 'dataset_idle/*.png')[:1500]
print(len(img_list_co))

from sklearn.model_selection import train_test_split

# resize 이미지를 test(20%)/train(80%) dataset으로 나누기
train_img_list_co, val_img_list_co = train_test_split(img_list_co, test_size=0.2, random_state=2000)

# 각각의 test(20%)/train(80%) dataset 이미지 수 출력
print(len(train_img_list_co), len(val_img_list_co))

# 기본 경로 설정
train_img_dir = os.path.join(dataset, 'train', 'image')
train_label_dir = os.path.join(dataset, 'train', 'labels')
val_img_dir = os.path.join(dataset, 'test', 'image')
val_label_dir = os.path.join(dataset, 'test', 'labels')

# 디렉토리 생성
os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# 이미지 이동 함수
def move_images(image_list, img_dst_dir, label_dst_dir):
    for img_path in image_list:
        # 이미지 파일 이름
        filename = os.path.basename(img_path)
        print(img_path)
        # 라벨 경로 추정 (예: .tif → .png)
        label_path = img_path.replace('dataset_idle', 'idleoutput').replace('.png', '.txt')

        # 이미지와 라벨 이동
        shutil.copy(img_path, os.path.join(img_dst_dir, filename))
        shutil.copy(label_path, os.path.join(label_dst_dir, os.path.basename(label_path)))

# 이미지와 라벨 각각 이동
move_images(train_img_list_co, train_img_dir, train_label_dir)
move_images(val_img_list_co, val_img_dir, val_label_dir)

print("데이터 분할 및 복사가 완료되었습니다.")