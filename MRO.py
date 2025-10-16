class A:
    def show(self):
        print("A says hello")

class B(A):
    def show(self):
        print("B says hi")

class C(A):
    def show(self):
        print("C says hey")

class D(C, B):
    pass

d = D()
d.show()
