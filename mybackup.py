import os, os.path, errno, sys, hashlib

myArchive = os.path.expanduser("~/Desktop/myArchive")
myObjects = os.path.expanduser(os.path.join(myArchive,'objects'))
indexFile = os.path.expanduser(os.path.join(myArchive,'index.html'))


def init():
    if not os.path.exists(myArchive):
        try:
            os.makedirs(myArchive)
        except OSError as e0:
            if e0.errno != errno.EEXIST:
                raise
    if not os.path.exists(myObjects):
        try:
            os.makedirs(myObjects)
        except OSError as e1:
            if e1.errno != errno.EEXIST:
                raise

    open(indexFile,"w")

def store():
    myPath = input("Your path please...")
    for files in os.listdir(myPath):
        # open(files,'r')
        print(createFileSig(files))


#==========================================================================
def createFileSig ():
#==========================================================================
    path = input("your path please...")
    f = None
    signature = None
    try:
        f = open(path, "rb")  # open for reading in binary mode
        hash = hashlib.sha1()
        s = f.read(16384)
        while (s):
            hash.update(s)
            s = f.read(16384)

        hashValue = hash.hexdigest()
        signature = (path,hashValue)
    except IOError:
        signature = None
    except OSError:
        signature = None
    finally:
        if f:
            f.close()

    return(signature)


# store = store()

sig = createFileSig()
print("SHA1 hash", sig)


#==========================================================================
#COMMAND LINE ACCESS
#==========================================================================

#print('Command line:', sys.argv)

# if sys.argv[1]=='init':
#     init()
# if sys.argv[1]=='store':
#     store()
# elif sys.argv[1]=='createFileSig':
#     createFileSig()

# elif sys.argv[1]=='test':
#     test()
# elif sys.argv[1]=='get':
#     get()
# else sys.argv[1]=='restore':
#     restore()

