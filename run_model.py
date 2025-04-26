import os
import json

# Base folder where ECE branches exist
base_path = r'D:\DESKTOP\Desktop\Final-year-project-015\Engineering\ECE'

# Get all subfolder names under ECE (representing topics)
subfolders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]

# Template content for files
index_html_content = "<!DOCTYPE html>\n<html>\n<head>\n  <title>Topic</title>\n  <link rel='stylesheet' href='style.css'>\n</head>\n<body>\n  <h1>Welcome to Topic</h1>\n  <script src='script.js'></script>\n</body>\n</html>"
script_js_content = "// JavaScript functionality goes here\nconsole.log('Hello from script.js');"
style_css_content = "/* Basic styles */\nbody { font-family: Arial, sans-serif; }"

# Loop through each topic folder
for folder in subfolders:
    topic_path = os.path.join(base_path, folder)
    topics_path = os.path.join(topic_path, 'Topics')

    # Create Topics folder if not exists
    os.makedirs(topics_path, exist_ok=True)

    # Create JSON file named after the subfolder
    json_file_path = os.path.join(topics_path, f'{folder}.json')
    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w') as json_file:
            json.dump({}, json_file, indent=4)

    # Create index.html, script.js, and style.css inside Topics
    files = {
        'index.html': index_html_content,
        'script.js': script_js_content,
        'style.css': style_css_content
    }

    for filename, content in files.items():
        file_path = os.path.join(topics_path, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(content)

print("Folders and files created successfully.")
