import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from Analysers.analyseDeprecatedConstructs import AnalyseDeprecatedConstructs

class TestDeprecatedConstructs(unittest.TestCase):

    testFile = "deprecatedConstructs"
    testDir = "./Tests/Analysers/"
    testPath = testDir+testFile

    def setUp(self):
        astFD = open(self.testPath+".ast","w")
        errFD = open(self.testPath+".err","w")
        p = subprocess.Popen(['solc','--ast-compact-json',self.testDir+'Contracts/'+self.testFile+'.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f',self.testPath+'.ast',self.testPath+'.err'])
        p.wait()
        
    def test_exceptions(self):
        parseAST = ParseAST()
        astFD = open(self.testPath+".ast","r")
        parseResults = parseAST.parse(astFD)
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        mapASTSourceToLineNumbers.analyser(self.testDir+"Contracts/"+self.testFile+".sol")
        analyseDeprecatedConstructs = AnalyseDeprecatedConstructs()
        analyseDeprecatedConstructs.analyser()
        self.assertEqual(len(analyseDeprecatedConstructs.statsTxOrigin), 1)
        self.assertEqual(analyseDeprecatedConstructs.statsTxOrigin[0]["line"], "21")
        self.assertEqual(len(analyseDeprecatedConstructs.statsBlockMembers), 1)
        self.assertEqual(analyseDeprecatedConstructs.statsBlockMembers[0]["line"], "7")
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
