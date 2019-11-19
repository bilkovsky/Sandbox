import sys
import os
import time
from multiprocessing import Pool
from functools import partial
import threading


def createFile(filename, pathtofiles, sizeoffiles, content):
    start = time.time()
    with open(pathtofiles + filename, 'w') as file:
        file.truncate(sizeoffiles)
        file.write(content)
        file.close()
    end = time.time()
    return end - start


if __name__ == '__main__':
    try:
        processes = 1
        pathToFiles = ''
        numberOfFiles = int(sys.argv[1])
        sizeOfFiles = int(sys.argv[2])
        if len(sys.argv) > 3:
            pathToFiles = sys.argv[3] + '\\'
            if len(sys.argv) > 4:
                processes = int(sys.argv[4])
        content = input("Input your content pattern : ")
        if not (os.path.exists(pathToFiles) or pathToFiles == ''):
            os.makedirs(pathToFiles)
        timeList = list()
        appStart = time.time()
        names = []
        pool = Pool(processes=processes)

        for i in range(0, numberOfFiles):
            names.append('test' + str(i + 1) + '.txt')

        timeList.append(pool.map(partial(createFile, pathtofiles = pathToFiles, sizeoffiles = sizeOfFiles,content = content), names))
        pool.close()
        pool.join()
        appEnd = time.time()
        timeList.sort()
        print(str(numberOfFiles) + " files created")
        print(str(appEnd - appStart))
        #print(str(len(timeList)))
        #print("Min : " + str(min(timeList)) + " Max : " + str(max(timeList)) + " Average : "
        #      + str(sum(timeList)/len(timeList)) + " Total : " + str(appEnd - appStart))

    except IndexError:
        print("Arguments count error, check your inputs")
    except ValueError:
        print("Some of your parameters are incorrect!")
    except Exception as e:
        print(e)
