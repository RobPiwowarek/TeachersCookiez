class Child:
    def __init__(self, testResult = 0, cookiez = 0):
        self.testResult = testResult
        self.cookiez = cookiez

    def __str__(self):
        return "%d : %d" % (self.testResult, self.cookiez)


