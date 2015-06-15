import subprocess
import codecs
import gzip
import bzip2

def zcat_read(fn):
    """ returns file handle that reads gzip files faster using zcat"""
    p = subprocess.Popen(["zcat", fn], stdout = subprocess.PIPE)
    f = StringIO(p.communicate()[0])
    logging.info("Using ZCAT, pid: "+str(p.pid))
    assert p.returncode ==0
    return f

def zcat_read(fn):
    """ returns file handle that reads gzip files faster using zcat"""
    p = subprocess.Popen(["zcat", fn], stdout = subprocess.PIPE)
    f = StringIO(p.communicate()[0])
    logging.info("Using ZCAT, pid: "+str(p.pid))
    assert p.returncode ==0
    return f

def open_file(fn, readwrite):
    """looks at filename fn, if last 3 characters is .gz will use gzip to process
    returns file object, readwrite is is usual r/w, for gzip files, it will append 'b'"""

    w = codecs.getwriter("utf-8")

    if fn[-3:] == '.gz': #gzip land
        #fix readwrite
        if readwrite == "r" or readwrite == "rb":
            return zcat_read(fn)
        elif readwrite == "w":
            readwrite = "wb"
        return w(gzip.open(fn,readwrite))
    elif fn[-4:] == '.bz2': #bzip land
        if readwrite in ("w","wb"):
            readwrite = "w"
        if readwrite in ("r","rb"):
            readwrite = "r"
        return w(bz2.BZ2File(fn,readwrite))
    elif readwrite in ['w','wb']:
        return w(open(fn,readwrite))
    else:
        return open(fn,readwrite)
