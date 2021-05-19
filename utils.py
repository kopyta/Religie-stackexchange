import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_data_frame(file_path):
    '''takes filepath .xml and returns dataframe'''
    try :
        with open(file_path, encoding='utf-8') as file:

            xml_data = ET.XML(file.read())
    except FileNotFoundError:
        raise Exception('Wrong file path')
    except ET.ParseError:
        raise Exception('Wrong encoding, or file type (needs utf8 .xml file)')

    return pd.DataFrame([row.attrib for row in xml_data])





if __name__=='__main__':
    '''test something'''



    pass