import os,sys,getopt

def args():
    fullCmdArguments = sys.argv

    # - further arguments
    argumentList = fullCmdArguments[1:]


    unixOptions = "htp"
    gnuOptions = ["help","test","production"]

    try:
        arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        sys.exit(2)

    for currentArgument, currentValue in arguments:
        if currentArgument in ("-t", "--test"):
            testScript = currentValue
            stageScript()
            print("It worked!!!!")
        elif currentArgument in ("-h", "--help"):
            print("-t test script before executing in production\n-h prints the help menu")
            exit()
        elif currentArgument in ("-p","--production"):
            prodScript()
        else:
            print("option not valid")



def stageScript():
    print("This is staging")
    os.system("free -m")
    os.system("df -h")

def prodScript():
    print("This is production")
    print("this is a test...")

def main():
    args()


main()
