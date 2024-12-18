class BisectionMethod:
    
    def __init__(self, Epsilon, a, b, func):
        
        print(f'<INFO> Step 1 - Definding f(x): {func}')
        self.InputChecking(0,f=func)

        print('<INFO> Step 1 -Done')
        self.func = func
        
        print('<INFO> Step 2 : Definding Values')
        self.InputChecking(1,a=a,b=b,e=Epsilon)

        print('<STEP> Step 2 - Done')
        self.a = a
        self.b = b
        self.E = Epsilon

        self.CalBegin()

    def InputChecking(self, Attribute, f=None, a=None, b=None, e=None):
        if Attribute == 0:
            pass
            Error = False
            if Error == True:
                raise SyntaxError(f'An Error Occurred while definding f(x):{f}')
        elif Attribute == 1:
            pass
    
    def CalBegin():
        pass
TwoFenFa =  BisectionMethod()
TwoFenFa.CalBegin(0.01,1,2,'x + 2')