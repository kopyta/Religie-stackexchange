import pandas as pd
import xml.etree.ElementTree as ET
import re


def rmtags(str):

    return re.sub(r'<.*?>|[\\\.\,\';":\(\)\!\?]', "", str.replace('\n', ' '))

def xml_to_data_frame(file_path):
    """takes filepath .xml and returns dataframe"""
    try:
        with open(file_path, encoding='utf-8') as file:

            xml_data = ET.XML(file.read())
    except FileNotFoundError:
        raise Exception('Wrong file path')
    except ET.ParseError:
        raise Exception('Wrong encoding, or file type (needs utf8 .xml file)')

    return pd.DataFrame([row.attrib for row in xml_data])


class Religion:
    """includes all dataframes connected with one religion"""

    def __init__(self, dictpath):
        """dictpath is a path to a dict with all 8 .xml files"""

        self.Badges = xml_to_data_frame(dictpath + "/Badges.xml")
        self.Comments = xml_to_data_frame(dictpath + "/Comments.xml")
        self.PostHistory = xml_to_data_frame(dictpath + "/PostHistory.xml")
        self.PostLinks = xml_to_data_frame(dictpath + "/PostLinks.xml")
        self.Posts = xml_to_data_frame(dictpath + "/Posts.xml")
        self.Tags = xml_to_data_frame(dictpath + "/Tags.xml")
        self.Users = xml_to_data_frame(dictpath + "/Users.xml")
        self.Votes = xml_to_data_frame(dictpath + "/Votes.xml")

    def clear_html_attrs(self):
        self.Posts['clear_body'] = [rmtags(string).strip() for string in self.Posts['Body']]

if __name__ == '__main__':
    '''test something'''


    pass



    pass