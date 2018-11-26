import logging, sys
from AnalyseAST.expression import AnalyseExpression
from AnalyseAST.variable import AnalyseVariable
from AnalyseAST.defUse import DefUseAnalysis
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers


class AnalyseReentrancy:

    statsPotentialReentrancy = []
    
    def analyser(self):
        expressions = AnalyseExpression.getAllExpressions()
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        logging.debug("\n<<<<<<<<<< Analyser: Reentrancy >>>>>>>>>>")
        
        calls = AnalyseExpression.getAllCalls()
        for call in calls:
            logging.debug("Call at line:" + str(mapASTSourceToLineNumbers.getLine(int(call.src.split(":",)[0]))))
            parent = call.parent
            found = False
            defs = []
            while(True):
                if (parent.nodeType == "ExpressionStatement"):
                    logging.debug("Found ExpressionStatement: " + str(parent.id))
                    found = True
                    break
                if (parent.nodeType == "ContractDefinition"):
                    break
                parent = parent.parent
            if (found):
                defs = DefUseAnalysis.getAllDefintionsAfterStatement(parent)
            defsOfStateVariables = []
            for _def in defs:
                logging.debug("_def: " + str(_def))
                logging.debug("Def: " + _def["name"] + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(_def["src"].split(":",)[0]))))
                variableID = _def["referencedDeclaration"]
                variables = AnalyseVariable.getAllVariables()
                for variable in variables:
                    if (variableID == variable.id and variable.stateVariable):
                        defsOfStateVariables.append(_def)
            if (len(defsOfStateVariables) != 0):
                self.statsPotentialReentrancy.append({
                    "line":str(mapASTSourceToLineNumbers.getLine(int(call.src.split(":",)[0]))),
                    "info":"potential reentrancy: state change after call()"
                })
                print("Potential Reentrancy: State change after call()")
            else:
                print("No Reentrancy: No state change after call()")

                    
                


        
