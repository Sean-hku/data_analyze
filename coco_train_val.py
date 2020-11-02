import os
import glob

txt_file = '../COCO/train'
file = open('../COCO/train.txt','w')
for path in glob.iglob(os.path.join(txt_file, "*.txt")):
    title, ext = os.path.splitext(os.path.basename(path))
    file.write('./data/COCO/JPEGImages/'+title+'.jpg'+ "\n")
file.close()
