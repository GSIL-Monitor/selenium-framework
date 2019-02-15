# -*- coding:utf-8 -*-

import csv  # excel lib
from configparser import ConfigParser  # ini lib
from xml.etree.ElementTree import ElementTree  # xml lib
from lib.common.log import logger


class ParseIni(object):
    def __init__(self, config_path):
        self.cf = ConfigParser()
        self.cf.read(config_path, encoding='UTF-8')

    def get_section_item(self, section_name):
        return dict(self.cf.items(section_name))

    def get_option_value(self, section_name, option_name):
        return self.cf.get(section_name, option_name)


class ParseExcel(object):
    def __init__(self, file_name):
        """
        initialize
        :param file_name: string, full path of file
        """
        self.file_name = file_name

    def write_excel(self, header, data):
        """
        Write Excel with list of header and dic data
        :param header: list, header names, ['age', 'name']
        :param data: dic list, [{'age':'20', 'name':'zhangsan'}, {'name':'lisi', 'age':'30'}]
        :return: N/A
        """
        with open(self.file_name, 'w',  newline="", encoding='utf-8') as f:
            writer = csv.DictWriter(f, header)
            writer.writeheader()
            writer.writerows(data)

    def read_excel(self):
        """
        Read Excel Data
        :return: ordered dic list
        """
        with open(self.file_name, 'r', newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))


class ParseXml:
    def __init__(self, file_name):
        """
        Constructor
        :param file_name: full path of xml file
        """
        self.file_name = file_name
        try:
            self.tree = ElementTree(file=self.file_name)
            self.root = self.tree.getroot()
        except Exception as e:
            logger.error(e)

    def get_attr_values(self, node_path, attr_name):
        """
        get the attribute value of some node
        :param node_path: node path where attribute locates
        :param attr_name:  attribute name
        :return: list of attribute values
        """
        try:
            attr_values = []
            nodes = self.root.findall(node_path)

            if len(nodes) > 0:
                for node in nodes:
                    attr_values.append(node.get(attr_name))

            return attr_values

        except Exception as e:
            logger.error(e)

    def get_node_text(self, parent_node, target_node):
        """
        get one or more child node text under the same parent node
        :param parent_node: parent node
        :param target_node: target node
        :return: dic of target node: key=tag name of parent node, value=text content of target node
        """
        try:
            dic_node_value = {}
            for nd in self.root.iter(parent_node):
                dic_node_value[nd.get('name')] = nd.find(target_node).text
            return dic_node_value
        except Exception as e:
            logger.error(e)

    def get_nodes_text_by_parent_name(self, parent_name, target_node):
        """
        get text list of target nodes
        :param parent_name: 'name' attribute value of parent node
        :param target_node: target node
        :return: text list of target nodes
        """
        try:
            list_text = []
            for nd in self.root.findall(".//*[@name='" + parent_name +"']//" + target_node):
                list_text.append(nd.text)
            return list_text
        except Exception as e:
            logger.error(e)

    def get_nodes(self, target_node):
        """
        get node obj
        :param target_node: target node
        :return: list of node obj
        """
        try:
            return self.root.findall(".//" + target_node)
        except Exception as e:
            logger.error(e)