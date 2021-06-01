make dataset for training with **only keywords** from google.



### Usage

```bash
python main.py -k "cat,dog" -n 5 
# -k, --keywords 
# -n, --nums  -> input total image count
# -r, --ratio -> train/val split ratio (default 0.2)
```



### Requirements

```bash
pip install -r requirements.txt
```



### Result

```bash
├── train
│   ├── cat
│   │   ├── 00002.jpg
│   │   ├── 00003.jpg
│   │   ├── 00004.jpg
│   │   └── 00005.jpg
│   └── dog
│       ├── 00002.jpg
│       ├── 00003.jpg
│       ├── 00004.jpg
│       └── 00005.jpg
└── val
    ├── cat
    │   └── 00001.jpg
    └── dog
        └── 00001.jpg

```





Depends on [google-image-download](https://github.com/hardikvasa/google-images-download)

