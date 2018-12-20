class Algorithm:
    def calculate_optimal(self, children):
        current_cookie = 1

        i = 0
        while i < len(children):
            children[i].cookiez = max(current_cookie, children[i].cookiez)

            if i == len(children)-1:
                break

            if children[i].testResult < children[i+1].testResult:
                current_cookie = current_cookie + 1
            else:
                current_cookie = 1

            i = i+1

        current_cookie = 1

        i = len(children)-1
        while i >= 0:
            children[i].cookiez = max(current_cookie, children[i].cookiez)

            if i == 0:
                break

            if children[i].testResult < children[i-1].testResult:
                current_cookie += 1
            else:
                current_cookie = 1

            i = i - 1


        for pos, child in enumerate(children):
            print("pos: " + str(pos) + " cookiez: " + str(child.cookiez) + " test result: " + str(child.testResult) + "\n")

