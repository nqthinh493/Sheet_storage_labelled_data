
# Google Sheet Storage Labelled-Data

Using Google Sheet API to download and upload data to Sheet


## Quick start
- [DATA](https://drive.google.com/drive/folders/1Wf0WYIKLlyrA6K-ViZksxvhJDNxvO4m_?usp=share_link)
- [LABEL TOOL](https://www.robots.ox.ac.uk/~vgg/software/via/via.html)
### Installation
##### 1. Clone repo
```bash
  git clone https://github.com/nqthinh493/Sheet_storage_labelled_data
```
##### 2. Install Google Client API
```bash
  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

##### 3. Install requirements.txt
```bash
  cd /to/the/repo/path

  pip install -r requirements.txt
```

### Label data
##### 1. Label mask for data by [Via](https://www.robots.ox.ac.uk/~vgg/software/via/via.html) of VGG tools, choose "Add files" to add necessary labelled-files
##### 2. Save Annotation file choose Annotation/Export Annotation (as CSV) on header-bar of Via tools
##### 3. Change current path of CSV Annotation files in ```main.py```
```bash
  CSV_PATH = 'D:/Downloads/via_annotation.csv' 
  to
  CSV_PATH = 'YOUR CURRENT PATH HERE' 
```
##### 4. To start Upload labelled-data, run main.py or run the following command

```bash
  python main.py
```


## Authors

- [@nqthinh493](https://www.github.com/octokatherine)

