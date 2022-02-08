import sys
sys.path.insert(0, 'schema/')
from binding import pubchem, desi_exp
import pymongo
import urllib
from os.path import exists