import json
import csv
import xml.etree.cElementTree as ET


original_file = open("final_students.txt", 'r')


def txt_to_dict():
    data_dict = []
    for column in original_file:
        sub_dictionary = {}
        stud_info = column.strip().split(",")

        for key_value in stud_info:
            info = key_value.strip().split(":")
            sub_dictionary[info[0]] = info[1]

        data_dict.append(sub_dictionary)
    return data_dict


def save_dict_to_json():
    data_dict = txt_to_dict()
    original_file
    with open('data.json', 'w') as outfile:
        json.dump(data_dict, outfile, indent=2)
    original_file.close()


def dict_to_csv():

    with open('data.json') as json_file:
        data = json.load(json_file)
        student_data = data
        data_file = open('data.csv', 'w')
        csv_writer = csv.writer(data_file)
        count = 0

    for student in student_data:
        if count == 0:

            header = student.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(student.values())

    data_file.close()


def json_xml():

    with open("data.json") as json_file:
        data = json.load(json_file)
        print(data)
        root = ET.Element("root")

    for z in data:
        ET.SubElement(root, "id").text = z["id"]
        ET.SubElement(root, "firstname").text = z["firstname"]
        ET.SubElement(root, "lastname").text = z["lastname"]
        ET.SubElement(root, "password").text = z["password"]

    # print(z)

    a = ET.ElementTree(root)

    # print(a)

    return a


def write_to_xml_file():
    xml_var = json_xml()
    xml_var.write('data.xml')


if __name__ == "__main__":

    input_field = int(
        input("Welcome choose your selection \n 1 to convert to json \n 2 to convert in csv \n\n input here:  "))

    if input_field == 1:
        save_dict_to_json()

    elif input_field == 2:
        dict_to_csv()

    elif input_field == 3:
        write_to_xml_file()
    else:
        print("Wrong input bye! Possible options are 1,2, or 3")
