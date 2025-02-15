import os

def remove_color_texcoord_lines():
    cwd = os.getcwd()
    
    vb0_file = None
    for file_name in os.listdir(cwd):
        if "vb0" in file_name and file_name.endswith(".txt"):
            vb0_file = file_name
            break 
    
    if vb0_file:
        file_path = os.path.join(cwd, vb0_file)
        

        with open(file_path, 'r') as file:
            lines = file.readlines()
        

        filtered_lines = [line for line in lines if 'COLOR' not in line and 'TEXCOORD' not in line]
        
 
        with open(file_path, 'w') as file:
            file.writelines(filtered_lines)
        
        print(f"Processed file: {vb0_file}")
    else:
        print("No file with 'vb0' in the name found in the current working directory.")

# Call the function
remove_color_texcoord_lines()
