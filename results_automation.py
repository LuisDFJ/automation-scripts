import csv
import os

def get_files_by_name( dir, filename ):
    file_list = []
    for root,_,files in os.walk( dir ):
        for file in files:
            if file == filename:
                filepath = os.path.join( root, file )
                restype = os.path.basename( root ).split( "_" )[-1]
                file_list.append( ( filepath, restype ) )

    file_list.sort( key=lambda x : float( x[1][:-2] ) )
    return file_list

class CFileReader:
    def __init__( self, files ):
        self.files = files
        self.pfiles = []
        self.readers = []

    def __enter__( self ):
        for file, _ in self.files:
            pfile = open( file, "r" )
            self.pfiles.append( pfile )
            print( f"File opened: ...{file[-50:-1]}" )
            reader = csv.reader( pfile, delimiter='\t' )
            next( reader )
            self.readers.append( reader )

    def __exit__(self, exc_type, exc_value, exc_traceback):
        for pfile in self.pfiles:
            print( f"File closed: ...{pfile.name[-50:-1]}" )
            pfile.close()
        self.pfiles = []
        self.readers = []

    def next( self ):
        entry = []
        for reader in self.readers:
            row = next( reader, None )
            if row == None:
                return None
            entry.append( row[ -1 ] )
        return entry

    def names( self ):
        name_list = []
        for _,name in self.files:
            name_list.append( name )
        return name_list

def wrap_results( dirname, filename ):
    resfilename = filename.split('.')[0] + '.txt'
    files = get_files_by_name( dirname, filename )
    reader = CFileReader( files )
    with reader:
        names = reader.names()
        with open( os.path.join( dirname, resfilename ), 'w', newline='' ) as pfile:
            writer = csv.writer( pfile, delimiter='\t' )
            writer.writerow( names )
            while True:
                row = reader.next()
                if row == None: break
                writer.writerow( row )

def get_results( root, filenames ):
    for element in os.listdir(root):
        path = os.path.join( root, element )
        if os.path.isdir( path ):
            for filename in filenames:
                wrap_results( path, filename )


filenames = [
    "Directional Deformation X.xls",
    "Directional Deformation Y.xls",
    "Directional Deformation Z.xls",
    "Equivalent Stress.xls"
]

get_results( r".\results\v1.2-results", filenames )