import get_parsed_files as _get_parsed_files
import csv as _csv

def groups_to_csv(class_items):
    
    sorted_classes = sorted(class_items.items(), key=lambda x: x[1], reverse=True)
    
    num_groups = 5
    groups = [[] for _ in range(num_groups)]
    group_times = [0]*5
    
    for class_name, time in sorted_classes:
        min_group_index = group_times.index(min(group_times))
        groups[min_group_index].append((class_name,time,min_group_index+1))
        # print(group_times[min_group_index])
        group_times[min_group_index] = group_times[min_group_index] + time


       
    with open('output.csv', 'w', newline='') as file:
        writer = _csv.writer(file)
        writer.writerow(['Classname', 'Time', 'GroupNo'])
        for group in groups:
            for class_name, time, group_index in group:
                writer.writerow([class_name, time, group_index])
                
    return groups


if __name__ == '__main__':
    data_folder = r'C:\Users\ayanb\Desktop\devops-assignment-main\programming\assignment-1\data2'
    class_items = _get_parsed_files.parse_xml_files(data_folder)
    group_classes = groups_to_csv(class_items)

