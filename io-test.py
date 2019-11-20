import sys
import os
import time
import threading

#io-test.py 5 102400000 "C:\temp\Mellanox Homework\Task3" 2


def createFile():
    while len(names) > 0:
        lock.acquire()
        start = time.time()
        if len(names) > 0:
            name = names.pop(0)
        print(str(threading.current_thread()) + " " + name)

        with open(pathToFiles + name, 'w') as file:
            file.truncate(sizeOfFiles)
            file.write(content)
            #file.close()
        end = time.time()
        timeList.append(end - start)
        lock.release()




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
        appStart = time.time()
        names = []
        threadList = []
        lock = threading.Lock()
        for i in range(0, numberOfFiles):
            names.append('test' + str(i + 1) + '.txt')
        for i in range(0, threads):
            t = threading.Thread(target=createFile,args=())
            threadList.append(t)
            t.start()
        for i in range(0, threads):
            threadList[i].join()
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
