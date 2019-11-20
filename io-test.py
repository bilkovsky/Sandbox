import sys
import os
import time
from multiprocessing import  Pool,Queue,Manager
from functools import partial
import threading

#io-test.py 5 102400000 "C:\temp\Mellanox Homework\Task3" 2


def createFile(filename, pathtofiles, sizeoffiles, content,q):
    start = time.time()
    #print(filename + " is started")
    with open(pathtofiles + filename, 'w') as file:
        file.truncate(sizeoffiles)
        file.write(content)
        file.close()
    #print(filename + " is finished  ")
    end = time.time()
    q.put(end - start)
    #timeList.append(end - start)


if __name__ == '__main__':
    try:
        threads = 1
        pathToFiles = ''
        numberOfFiles = int(sys.argv[1])
        sizeOfFiles = int(sys.argv[2])
        if len(sys.argv) > 3:
            pathToFiles = sys.argv[3] + '\\'
            if len(sys.argv) > 4:
                threads = int(sys.argv[4])
        content = input("Input your content pattern : ")
        if not (os.path.exists(pathToFiles) or pathToFiles == ''):
            os.makedirs(pathToFiles)
        timeList = list()

        names = []
        m = Manager()
        q = m.Queue()
        pool = Pool(processes = threads)
        for i in range(0, numberOfFiles):
            names.append('test' + str(i + 1) + '.txt')
        appStart = time.time()
        pool.map(partial(createFile, pathtofiles=pathToFiles, sizeoffiles=sizeOfFiles, content=content,q = q), names)
        pool.close()
        pool.join()
        appEnd = time.time()
        for i in range(0, numberOfFiles):
            timeList.append(q.get())
        timeList.sort()
        print(str(numberOfFiles) + " files created in " + pathToFiles + " in " + str(threads) + " threads")
        #print(appEnd - appStart)
        print("Min : " + str(min(timeList)) + " Max : " + str(max(timeList)) + " Average : "
              + str(sum(timeList)/len(timeList)) + " Total : " + str(appEnd - appStart))

    except IndexError:
        print("Arguments count error, check your inputs")
    except ValueError:
        print("Some of your parameters are incorrect!")
    except Exception as e:
        print(e)
