from pip._vendor import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import csv
import re

# This is for WVU Institute of technology courses

def pull_data():
    # # Send HTTP request
    url = f"http://catalog.wvu.edu/westvirginiauniversityinstituteoftechnology/courses/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    course_data = soup.find_all(class_="courseblocktitle")
    description_data = soup.find_all(class_="courseblockdesc")
    return course_data, description_data


def pull_course_description():
    # # Send HTTP request
    url = f"http://catalog.wvu.edu/westvirginiauniversityinstituteoftechnology/courses/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    raw_data = soup.find_all(class_="courseblockdesc")
    return raw_data


def parse_course(raw_data):
    temp_list = []
    result_list = []
    try:
        for div in raw_data:
            div = str(div)
            w = div[36:len(div)]
            x = w[0:10]
            y = x.split(".")
            temp_list.append(y[0])
            for result in temp_list:
                result_list.append(result)
        courses = []
        [courses.append(x) for x in result_list if x not in courses]
        return courses
    except Exception as e:
        print(f"Error parsing html data {e}")


def parse_description(raw_data):
    result_list = []
    for div in raw_data:
        div = str(div)
        w = div[25:len(div)]
        x = w[0:len(w)-10]
        x = x.replace('">', '')
        while "<a class=" in x:
            start = x.find("<a class=")
            end = x.find("</a>") + len("</a>")
            y = x[start:end]
            x = x.replace(y, '')
        result_list.append(x)
        print(x)
    return result_list


def data_to_csv(courses, descriptions):
    file = open("Z:\\dev now\\scrapeWvuCourses\\data\\wvu_detailed_course_list.csv", 'a+', newline='')

    with file:
        write = csv.writer(file)
        for x in range(len(courses)):
            write.writerow([courses[x], descriptions[x]])


if __name__ == "__main__":
    course_data, description_data = pull_data()
    courses = parse_course(course_data)
    descriptions = parse_description(description_data)
    data_to_csv(courses, descriptions)

