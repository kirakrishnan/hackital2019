import io
import os
import csv

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

from shutil import copyfile


# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name_1 = os.path.join(
    os.path.dirname(__file__),
    'resources/wakeupcat.jpg')
file_name = 'test_003.jpg'


##gets the text from the image
def get_text(file_name):
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.text_detection(image=image)
    labels = response.text_annotations

    text_in_image = []
    for label in labels:
        text_in_image.append(label.description)
    return text_in_image

print(get_text("/Users/aravind/PycharmProjects/personalprojects/hackital2019/streetparking/valid_plates/test_016.jpg"))


##gets the text from the image
def get_all_texts(file_name):
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.text_detection(image=image)
    labels = response.text_annotations

    text_in_image = []
    for label in labels:
        text_in_image.append(label.description)
    return text_in_image


#runs each image thru the get_text function and prints the plate number from each image
def get_all_text():
    count = 0
    # for path, subdirs, files in os.walk(r'/Users/aravind/PycharmProjects/practise/snapshots'):
    for path, subdirs, files in os.walk(r'/Users/aravind/PycharmProjects/personalprojects/hackital2019/streetparking/valid_plates'):
       for filename in files:
         f = path +"/"+ os.path.join(filename)

         result = get_text(f)
         destination = "/Users/aravind/PycharmProjects/practise/valid_plates/"+filename
         texts = result[0].split("\n")
         for text in texts:
                 if(" " in text or "-" in text):
                     print(filename, end=":")
                     print(text)
    print(count)

# count = 0
# # for path, subdirs, files in os.walk(r'/Users/aravind/PycharmProjects/practise/snapshots'):
# for path, subdirs, files in os.walk(r'/Users/aravind/PycharmProjects/practise/valid_plates'):
#    for filename in files:
#      f = path +"/"+ os.path.join(filename)
#      print(filename,end=":")
#      result = get_text(f)
#      print(result)
#      destination = "/Users/aravind/PycharmProjects/practise/valid_plates/"+filename
#      if(len(result)==0):
#          count += 1
#      else:
#          # copyfile(f,destination)
#         pass


# read the csv file and insert the corespondong plate no
def match_plate_no():
    platnos = {}
    with open("test23.txt") as f:
        lines = f.readlines()
        for line in lines:
            try:
                image, carno = line.split(":")
                platnos[image] = carno
            except:
                print(line)
    print(platnos)
    records_plateno = []
    with open('license_plate_data.csv') as csv_file:
        for line in csv_file:
            plate_details = line.split(",")
            image_id = plate_details[-1].rstrip("\n")
            try:
                plate_details[-1] = plate_details[-1].rstrip("\n")
                plate_details.append(platnos[image_id].rstrip("\n"))
                records_plateno.append(plate_details)
            except:
                print(image_id)
            # print(records_plateno)

    with open('license_plate_with_values.csv', mode='w') as csv_file2:
        plate_writer = csv.writer(csv_file2, delimiter=',')
        for line in records_plateno:
            plate_writer.writerow(line)
