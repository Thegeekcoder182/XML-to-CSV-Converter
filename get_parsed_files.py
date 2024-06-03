import os as _os
import xml.etree.ElementTree as _ET
from glob import glob as _glob
from collections import defaultdict as _defaultdict
 
def parse_xml_files(data_folder):
    class_times = _defaultdict(float) 
    xml_files = _glob(_os.path.join(data_folder, '*.xml'))  
 
    
    for xml_file in xml_files: 
        tree = _ET.parse(xml_file) 
        
        root = tree.getroot()  
        
        class_total_time = 0.0
        for testcase in root.findall('testcase'):
            classname = testcase.attrib.get('classname')
            time_sum = float(testcase.attrib.get('time',0))
            class_total_time = class_total_time+time_sum
            
        class_times[classname] = class_total_time
            
    return class_times
