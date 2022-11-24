def func( Pa, Pb ):
    m = ( Pb[1] - Pa[1] ) / ( Pb[0] - Pa[0] )
    b = Pb[1] - m * Pb[0]
    return lambda x: m * x + b

def vector( domain, step, f ):
    X = []; Y = []
    n = int( ( domain[1] - domain[0] ) / step )
    for i in range( n ):
        x = i * step + domain[0]
        y = f( x )
        X.append( round( x, 2 ) )
        Y.append( round( y, 2 ) )
    return X, Y

def linspace( domain, steps ):
    h = ( domain[1] - domain[0] ) / steps
    X = [ round( i * h + domain[0], 2 ) for i in range( steps ) ]
    X.append( domain[1] )
    return X

x = linspace( [-5, -4], 5 )
print( x )