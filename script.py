
import os
import shutil
import sys

def getUniqueFileName(dest_dir, filename):
    base, end = os.path.splitext(filename)
    counter = 1
    while os.path.exists(os.path.join(dest_dir, filename)): 
        filename = f"{base}_{counter}{end}"
        counter += 1
    return filename

def main():
    inputDir = sys.argv[1]
    outputDir = sys.argv[2]
    
    for root, sub, files in os.walk(inputDir):
        for file in files:
            curPath = os.path.join(root, file)
            newFilename = getUniqueFileName(outputDir, file)
            newPath = os.path.join(outputDir, newFilename)
            shutil.copy2(curPath, newPath)

if __name__ == "__main__":
    main()