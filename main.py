from bs4 import BeautifulSoup
import ast
import numpy as np
import cv2
from skimage import io
import matplotlib.pyplot as plt







############****************************################################








img_info_url="/Users/zola/Desktop/image_highlighter/imagenet_val_sample/ILSVRC2012_val_00000002.xml"

with open(img_info_url, 'r') as f:
    txtdata = f.read()


# print(data)


bs_data=BeautifulSoup(txtdata,"xml")


imageName=bs_data.find_all("name")
imageSize=bs_data.find_all("bndbox")



coordinate_list=[]
name_list=[]

for line in imageName:
  theLine=line.get_text().strip()
  theLine=theLine.replace("n","")
  name_list.append(theLine)

print(name_list)

each_line_list=[]


for item in imageSize:
  each_line=item.get_text().strip()
  each_line_list.append(each_line)



string_list=[]


for item in each_line_list:
  string_list.append(item.split("\n"))

for item in string_list:
  list_within=[]
  for i in item:
    i=int(i)
    list_within.append(i)
  coordinate_list.append(list_within)


print(coordinate_list)



# ****************************************************************************



import ast
gitrepoUrl="/Users/zola/Desktop/image_highlighter/gitRepo/imagenet_label_to_wordnet_synset.txt"

# Read the contents of the text file
with open(gitrepoUrl, 'r') as file:
    file_content = file.read()

# Safely evaluate the string representation of the dictionary
data_dict = ast.literal_eval(file_content)

# Verify the conversion
print(data_dict)

id_label_dict={}

for key in data_dict:
  for key2 in data_dict[key]:
    id=data_dict[key]['id'].replace("-n","")
    if id in name_list:
      if id in id_label_dict:
        id_label_dict[id].append([data_dict[key]['label']])
      id_label_dict[id]=[data_dict[key]['label']]
    break 

print(id_label_dict)







###################***********_____________________****************##########






imageURL="/Users/zola/Desktop/image_highlighter/imagenet_val_sample/ILSVRC2012_val_00000002.JPEG"
image = io.imread(imageURL)

for i in range(len(coordinate_list)):
  cv2.rectangle(image,(coordinate_list[i][0],coordinate_list[i][1]),(coordinate_list[i][2],coordinate_list[i][3]),color=(255,0,0), thickness=2)
  cv2.putText(image, id_label_dict[name_list[i]][0], (coordinate_list[i][0]+2, coordinate_list[i][1]+100), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,110), 2)


plt.imshow(image)

plt.show()