import os

def save_res( path, parameter ):
    path = os.path.join( path, "res_{}mm".format(parameter) )
    
    if not os.path.isdir( path ):
        os.makedirs( path )
        print( "{} ... created".format(path) )
    
    for i in range( 1,5 ):
        result = Model.Analyses[0].Solution.Children[i]
        rPath = os.path.join( path, "{}.xls".format(result.Name) )
        result.ExportToTextFile( rPath )
        print( "Results saved at: {}".format( rPath ) )

def change_dis( dis ):
    nDis = Quantity( dis, "mm" )
    XDis = Model.Analyses[0].Children[2].XComponent
    XDis.Output.SetDiscreteValue(0, nDis )

def train():
    path = r"C:\Users\A01702840\Desktop\results\11-18-2022-train"
    parameters = [ -12, -10, -8, -6,-4, -2, 0, 2, 4, 6, 8, 10, 12 ]
    for parameter in parameters:
        change_dis( parameter )
        Model.Analyses[0].Solve()
        status = str( Model.Analyses[0].Solution.Status )
        if status != 'SolveRequired':
            save_res( path, parameter )

def test():
    path = r"C:\Users\A01702840\Desktop\results\11-18-2022-test"
    parameters = [ -5,3, 13, -11.5 ]
    for parameter in parameters:
        change_dis( parameter )
        Model.Analyses[0].Solve()
        status = str( Model.Analyses[0].Solution.Status )
        if status != 'SolveRequired':
            save_res( path, parameter )

def main():
    print( "Running Trainning Data" )
    train()
    print( "Running Testing Data" )
    test()

main()