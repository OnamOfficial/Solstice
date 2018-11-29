import unittest
import subprocess, os, sys

class TestAnalysers(unittest.TestCase):

    analyser1 = "analyseContractFeatures"
    analyser2 = "analyseControlFlowGraph"
    analyser3 = "analyseDefaultVisibility"
    analyser4 = "analyseDeprecatedConstructs"
    analyser5 = "analyseDoSWithBlockGasLimit"
    analyser6 = "analyseDoSWithUnexpectedRevert"
    analyser7 = "analyseDoSWithUnexpectedRevertLoop"
    analyser8 = "analyseExternalContractInteractions"
    analyser9 = "analyseExceptions"
    analyser10 = "analyseReentrancy"
    analyser11 = "analyseUncheckedCalls"
    analyser12 = "analyseUncheckedSelfDestructs"
    analyser13 = "analyseUninitialisedStoragePointers"
    analyser14 = "analyseDefsUses"
    totalAnalysers = '14'
    
    testDir = "./Tests/Analysers/"
    
    def setUp(self):
        outFD = open(self.testDir + "testOutput.out","w+")
        p1 = subprocess.Popen(['python3',self.testDir+self.analyser1 +'.py'], stdout=outFD, stderr=outFD)
        p1.wait()
        p2 = subprocess.Popen(['python3',self.testDir+self.analyser2 +'.py'], stdout=outFD, stderr=outFD)
        p2.wait()
        p3 = subprocess.Popen(['python3',self.testDir+self.analyser3 +'.py'], stdout=outFD, stderr=outFD)
        p3.wait()
        p4 = subprocess.Popen(['python3',self.testDir+self.analyser4 +'.py'], stdout=outFD, stderr=outFD)
        p4.wait()
        p5 = subprocess.Popen(['python3',self.testDir+self.analyser5 +'.py'], stdout=outFD, stderr=outFD)
        p5.wait()
        p6 = subprocess.Popen(['python3',self.testDir+self.analyser6 +'.py'], stdout=outFD, stderr=outFD)
        p6.wait()
        p7 = subprocess.Popen(['python3',self.testDir+self.analyser7 +'.py'], stdout=outFD, stderr=outFD)
        p7.wait()
        p8 = subprocess.Popen(['python3',self.testDir+self.analyser8 +'.py'], stdout=outFD, stderr=outFD)
        p8.wait()
        p9 = subprocess.Popen(['python3',self.testDir+self.analyser9 +'.py'], stdout=outFD, stderr=outFD)
        p9.wait()
        p10 = subprocess.Popen(['python3',self.testDir+self.analyser10 +'.py'], stdout=outFD, stderr=outFD)
        p10.wait()
        p11 = subprocess.Popen(['python3',self.testDir+self.analyser11 +'.py'], stdout=outFD, stderr=outFD)
        p11.wait()
        p12 = subprocess.Popen(['python3',self.testDir+self.analyser12 +'.py'], stdout=outFD, stderr=outFD)
        p12.wait()
        p13 = subprocess.Popen(['python3',self.testDir+self.analyser13 +'.py'], stdout=outFD, stderr=outFD)
        p13.wait()
        p14 = subprocess.Popen(['python3',self.testDir+self.analyser14 +'.py'], stdout=outFD, stderr=outFD)
        p14.wait()
        outFD.close()

        
    def tearDown(self):
        p1 = subprocess.Popen(['rm','-f',self.testDir+'testCheck.out'])
        p1.wait()
        p2 = subprocess.Popen(['rm','-f',self.testDir+'testOutput.out'])
        p2.wait()
        

    
    def test_analysers(self):
        outFD = open(self.testDir + "testCheck.out","w")
        p1 = subprocess.Popen(['grep','-c','OK',self.testDir+'testOutput.out'], stdout=outFD)
        p1.wait()
        outFD.close()
        outFD = open(self.testDir + "testCheck.out","r")
        lines = outFD.readlines()
        self.assertEqual(lines[0].rstrip(), self.totalAnalysers)
        outFD.close()
        p2 = subprocess.Popen(['grep','FAIL','-A7',self.testDir+'testOutput.out'])
        p2.wait()
        
if __name__ == '__main__':
    unittest.main()
