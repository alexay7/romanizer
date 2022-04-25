import pykakasi
import os
import re

kks = pykakasi.kakasi()

def main():
    ROUTE = "C:\\Users\\user"
    MAXDEPTH=1

    while MAXDEPTH>0:
        for root,dirs,files in os.walk(ROUTE):
            for dir in dirs:
                os.chdir(root)
                text = dir
                converted = kks.convert(text)
                result=""
                for item in converted:
                    result+=item["hepburn"]
                os.rename(dir,re.sub(r'[^\w\-_\. ]', '_', result))

            for file in files:
                os.chdir(root)
                text = file
                converted = kks.convert(text)
                result=""
                for item in converted:
                    result+=item["hepburn"]
                os.rename(file,re.sub(r'[^\w\-_\. ]', '_', result))
        MAXDEPTH-=1

if __name__ == '__main__':
    main()
