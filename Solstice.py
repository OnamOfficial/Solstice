import subprocess, os, sys, getopt
from ParseAST.parseAST import ParseAST
from Analysers.analyseExternalContractInteractions import AnalyseExternalContractInteractions
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers

class Solstice:
    inputFile = ""
    outputFile = ""
    astFile = ""
    errFile = ""
    
    def main(self, argv):
        try:
            opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
        except getopt.GetoptError:
            print("Solstice.py -i <Input Solidity File> -o <Output Report File>")
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print("Solstice.py -i <Input Solidity File> -o <Output Report File>")
                sys.exit()
            elif opt in ("-i", "--ifile"):
                self.inputFile = arg
            elif opt in ("-o", "--ofile"):
                self.outputFile = arg
        print("Input file is ", self.inputFile)
        print("Output file is ", self.outputFile)

    def process(self):
        self.astFile = self.inputFile + ".ast"
        self.errFile = self.inputFile + ".err"
        astFD = open(self.astFile,"w")
        errFD = open(self.errFile,"w")
        p = subprocess.Popen(['solc','--ast-compact-json',self.inputFile], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def analyse(self):
        parseAST = ParseAST()
        astFD = open(self.astFile,"r")
        parseResults = parseAST.parse(astFD)
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        mapASTSourceToLineNumbers.analyser(self.inputFile)
        analyseExternalContractInteractions = AnalyseExternalContractInteractions()
        analyseExternalContractInteractions.analyser()
        astFD.close()
        
if __name__ == "__main__":
    solstice = Solstice()
    solstice.main(sys.argv[1:])
    solstice.process()
    solstice.analyse()
   

