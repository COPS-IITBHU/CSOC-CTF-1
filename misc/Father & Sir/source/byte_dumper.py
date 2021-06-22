import base64
import os

directory ="" #fill me

def bytesTob64(chunk):
    return base64.b64encode(chunk)
def b64toBytes(b64code):
    return base64.b64decode(b64code.encode('ascii'))
    
'''Provide folder path to pngs and it will encode the bytes into b64
   and write them to picsflags.txt'''    
def createB64Dumps(folder):
    flags=open(folder+'flags.txt','w')
    for filename in os.listdir(folder):
        file = os.path.join(folder, filename)
        # checking if it is a file
        if os.path.isfile(file):
            chunk=b''
            with open(file,'rb') as (stream):
                chunk=stream.read()
                    
            flags.write(bytesTob64(chunk).decode('ascii'))
            flags.write('\n')
            flags.write('\n')
            flags.write('\n')

'''Provide path to picsflags.txt and it will decode b64 into bytes
   and write them out into separate pngs '''             
def createPngDumps(flags):
    flags=open(flags,'r')
    lines=flags.readlines()
    print('found {0} lines '.format(len(lines)))
    it=1
    for line in lines:
        png=open(directory+'\\{0}.png'.format(it),"wb")
        png.write(b64toBytes(line))
        png.close()
        it=it+1
    
if __name__ == "__main__":
    #createPngDumps(directory+'flags.txt')       
    createB64Dumps(directory)