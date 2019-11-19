import sys
import os
import time
from multiprocessing import Pool

def createFile(filename):
    start = time.time()
    with open(pathToFiles + filename, 'w') as file:
        file.truncate(sizeOfFiles)
        file.write(content)
        file.close()
    end = time.time()
    timeList.append(end - start)

try:
    pathToFiles = ''
    numberOfFiles = int(sys.argv[1])
    sizeOfFiles = int(sys.argv[2])
    if len(sys.argv) > 3:
        pathToFiles = sys.argv[3] + '\\'
    if not (os.path.exists(pathToFiles) or pathToFiles == ''):
        print("Such directory doesnt exist")
        exit(0)
    content = input("Input your content pattern : ")
    timeList = list()
    appStart = time.time()
    for i in range(0,numberOfFiles):
        createFile('test' + str(i + 1) + '.txt')
    appEnd = time.time()
    timeList.sort()
    print(str(numberOfFiles) + " files created")
    print("Min : " + str(min(timeList)) + " Max : " + str(max(timeList)) + " Average : "
          + str(sum(timeList)/len(timeList)) + " Total : " + str(appEnd - appStart))

except IndexError:
    print("Arguments count error, check your inputs")
except ValueError:
    print("Some of your parameters are incorrect!")
except Exception as e:
    print(e)
